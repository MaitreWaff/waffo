from django.db.models import permalinkfrom django.template.defaultfilters import slugifyfrom profiles.models import Profilefrom time import timefrom django.db import models# CONSTANTESMAX_L_AUTHEUR   = 150MAX_THEME_LENGTH= 100MAX_TAG_LENGTH  = 50MAX_L_TITRE     = 150MAX_L_CONTENU   = 1000MAX_L_SLUG      = 128# Retourne le Nom De l'Image telechargee.def get_upload_blog_file_name(instance, filename):    return "uploaded_files/blogimages/%s_%s" % (str(time()).replace('.', '_'), filename)def get_upload_post_file_name(instance, filename):    return "uploaded_files/postimages/%s_%s" % (str(time()).replace('.', '_'), filename)# Managers# class BlogManager(models.Manager):#     def get_by_natural_key(self, auteur, theme, date_blog):#         return self.get(auteur=auteur, theme=theme, date_blog=date_blog)# Create your models here.class Blog(models.Model):    # objects = BlogManager()    auteur          = models.ForeignKey(Profile)#, related_name='blogs')    # OneToOneField(Profile, on_delete=models.CASCADE) #CharField(max_length=MAX_L_AUTHEUR) # User proprietaire du blog.    theme           = models.TextField(max_length=MAX_THEME_LENGTH, null=True, blank=True)    illustration    = models.FileField(upload_to=get_upload_blog_file_name, blank=True, null=True)    date_blog       = models.DateTimeField('Created On', auto_now_add=True, editable=False)    slug            = models.SlugField(blank=True, max_length=MAX_L_SLUG)    def __unicode__(self):        return "[%s] Blog: '%s' " % (self.auteur, self.theme)    @permalink    def get_absolute_url(self):        return ('blog-detail', (), {'slug': self.slug})    def save(self, *args, **kwargs):        if not self.slug:            self.slug = slugify(self.theme)            # self.slug = slugify(self.auteur.user.username)        super(Blog, self).save(*args, **kwargs)    def natural_key(self):        return (self.pk, self.auteur.user.username, self.theme, self.date_blog)    class Meta:        ordering = ('-date_blog',)        unique_together = (('auteur', 'theme', 'date_blog'))class BlogPost(models.Model):    titre           = models.CharField(max_length=MAX_L_TITRE)    illustration    = models.FileField(upload_to=get_upload_post_file_name, blank=True, null=True)    text            = models.TextField(max_length=MAX_L_CONTENU, default="(Empty.)") # description    date_post       = models.DateTimeField('Created On', auto_now_add=True, editable=False)    blog            = models.ForeignKey(Blog, related_name='posts')    slug            = models.SlugField(blank=True, max_length=MAX_L_SLUG)    def __unicode__(self):        return "[%s] %s" % (self.date_post, self.titre)    @permalink    def get_absolute_url(self):        return ('blogpost-details', (), {'slug': self.slug})    def save(self, *args, **kwargs):        if not self.slug:            self.slug = slugify(self.titre)        super(BlogPost, self).save(*args, **kwargs)    class Meta:        ordering = ('-date_post',)class CategorieTagAbstract(models.Model):    nom     = models.CharField(max_length=MAX_TAG_LENGTH, unique=True)    class Meta:        abstract = True    def __unicode__(self):        return "%s" % self.nomclass CategorieTag(CategorieTagAbstract):    passclass Tag(models.Model):    categorie       = models.ForeignKey(CategorieTag)    blogpost        = models.CharField(max_length=MAX_TAG_LENGTH)    def __unicode__(self):        return "%s" % self.categorieclass SectionAbstract(models.Model):    rang            = models.IntegerField(default=0) # chapitre #    titre           = models.CharField(max_length=MAX_L_TITRE)    illustration    = models.FileField(upload_to=get_upload_post_file_name, blank=True)  # image    text            = models.TextField(blank=True)    # image           = models.FileField(upload_to=get_upload_post_file_name, blank=True)    class Meta:        abstract = True        ordering = ('rang',)    def __unicode__(self):        return "%s" % self.titreclass BlogSection(SectionAbstract):    blogpost        = models.ForeignKey(BlogPost, related_name='blogsections')class SectionSection(SectionAbstract):    blogsection = models.ForeignKey(BlogSection, related_name='secsections')class CommentAbstrat(models.Model):    auteur      = models.ForeignKey(Profile)    #OneToOneField(Profile, on_delete=models.DO_NOTHING) # ForeignKey(Profile)    #CharField(max_length=MAX_L_AUTHEUR)    commentaire = models.TextField()    date_comm   = models.DateTimeField('Commented On', auto_now_add=True)    def __unicode__(self):        return "%s : %s" % (self.auteur, self.commentaire)class CommentBlogPost(CommentAbstrat):    blogpost = models.ForeignKey(BlogPost, related_name='postcomments')# Reply to a comment.class ReplyComment(CommentAbstrat):    comment     = models.ForeignKey(CommentBlogPost, related_name='replycomments')# Interactions: Like, Share.class InteractionAbstract(models.Model):    auteur  = models.ForeignKey(Profile)    #OneToOneField(Profile, on_delete=models.DO_NOTHING) #CharField(max_length=MAX_L_AUTHEUR)    def __unicode__(self):        return "%s" % self.auteur# Likesclass LikeAbstract(InteractionAbstract):    date_like   = models.DateTimeField('Liked On', auto_now_add=True, editable=False)    class Meta:        abstract = Trueclass LikeBlogPost(LikeAbstract):    blogpost = models.ForeignKey(BlogPost)class LikeCommentBlogPost(LikeAbstract):    comment     = models.ForeignKey(CommentBlogPost)class LikeReplyComment(LikeAbstract):    comment     = models.ForeignKey(ReplyComment)# Sharesclass ShareAbstract(InteractionAbstract):    date_share  = models.DateTimeField('Shared On', auto_now_add=True, editable=False)    class Meta:        abstract = Trueclass ShareBlogPost(ShareAbstract):    blogpost    = models.ForeignKey(BlogPost)