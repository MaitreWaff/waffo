from django.db import models# CONSTANTESMAX_L_AUTHEUR   = 150MAX_SUJET_LENGTH= 100MAX_TAG_LENGTH  = 50MAX_L_TITRE     = 150MAX_L_CONTENU   = 1000# Create your models here.class Blog(models.Model):    auteur      = models.CharField(max_length=MAX_L_AUTHEUR) # User proprietaire du blog.    sujet       = models.TextField(max_length=MAX_SUJET_LENGTH, null=True)    # illustration = models.ImageField()    def __unicode__(self):        return "%s" % self.auteurclass BlogPost(models.Model):    titre       = models.CharField(max_length=MAX_L_TITRE)    contenu     = models.TextField(max_length=MAX_L_CONTENU, default="(Empty.)") # description    date_post   = models.DateTimeField('Created On', auto_now_add=True)    blog        = models.ForeignKey(Blog)    class Meta:        ordering = ('-date_post',)    def __unicode__(self):        return "%s" % self.titreclass CategorieTagAbstract(models.Model):    nom     = models.CharField(max_length=MAX_TAG_LENGTH, unique=True)    def __unicode__(self):        return "%s" % self.nomclass CategorieTag(CategorieTagAbstract):    passclass Tag(models.Model):    categorie       = models.ForeignKey(CategorieTag)    blogpost        = models.CharField(max_length=MAX_TAG_LENGTH)    def __unicode__(self):        return "%s" % self.categorieclass SectionAbstract(models.Model):    numero_dordre   = models.IntegerField(default=0) # chapitre #    titre           = models.CharField(max_length=MAX_L_TITRE)    illustration    = models.CharField(max_length=MAX_L_TITRE, blank=True)  # image    paragraphe      = models.TextField(blank=True)    class Meta:        ordering = ('numero_dordre',)    def __unicode__(self):        return "%s" % self.titreclass BlogSection(SectionAbstract):    blogpost        = models.ForeignKey(BlogPost)class SectionSection(SectionAbstract):    blogsection = models.ForeignKey(BlogSection)class CommentAbstrat(models.Model):    auteur      = models.CharField(max_length=MAX_L_AUTHEUR)    commentaire = models.TextField()    date_comm   = models.DateTimeField('Commented On', auto_now_add=True)    def __unicode__(self):        return "%s" % self.commentaireclass CommentBlogPost(CommentAbstrat):    blogpost = models.ForeignKey(BlogPost)# Interactions: Like, Share.class InteractionAbstract(models.Model):    auteur  = models.CharField(max_length=MAX_L_AUTHEUR)    def __unicode__(self):        return "%s" % self.auteur# Likesclass LikeAbstract(InteractionAbstract):    date_like   = models.DateTimeField('Liked On', auto_now_add=True)class LikeBlogPost(LikeAbstract):    blogpost = models.ForeignKey(BlogPost)class LikeCommentBlogPost(LikeAbstract):    comment     = models.ForeignKey(CommentBlogPost)# Sharesclass ShareAbstract(InteractionAbstract):    date_share  = models.DateTimeField('Shared On', auto_now_add=True)class ShareBlogPost(ShareAbstract):    blogpost    = models.ForeignKey(BlogPost)