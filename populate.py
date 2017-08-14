import os

list_titres_bp = ['Premier Blog Post', 'Vive Les Blogs', 'Pourquoi ce Blog?', 'Vous avez dit Linux?', 'Certifications', 'Trainings', 'Materiel', 'Services', 'Telephones']
lorem_ipsum_text = "Iamque lituis cladium concrepantibus internarum non celate ut antea turbidum saeviebat ingenium a veri consideratione detortum et nullo inpositorum vel conpositorum fidem sollemniter inquirente nec discernente a societate noxiorum insontes velut exturbatum e iudiciis fas omne discessit, et causarum legitima silente defensione carnifex rapinarum sequester et obductio capitum et bonorum ubique multatio versabatur per orientales provincias, quas recensere puto nunc oportunum absque Mesopotamia digesta, cum bella Parthica dicerentur, et Aegypto, quam necessario aliud reieci ad tempus."
lorem_ipsum_text2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def populate():
    #from datetime import datetime
    #from django.utils import timezone

    for text in list_titres_bp:
        newbp = add_blog_post(text, lorem_ipsum_text)
        for mtr in list_titres_bp:
            newbps = add_comment_bp('Luc Waffo', lorem_ipsum_text2)

    reseau_cat       = add_cat_service('ADMINISTRATION MAINTENANCE DES SYSTEMES ET RESEAUX INFORMATIQUE.', 'ADMINISTRATION MAINTENANCE DES SYSTEMES ET RESEAUX INFORMATIQUE.')

    add_like_astuce('https://www.facebook.com/maitre.waff', art_un)
    add_like_astuce('https://myaccount.google.com/?utm_source=OGB&pli=1', art_un)

    add_like_info('https://www.facebook.com/maitre.waff', inf_un)
    add_like_info('https://myaccount.google.com/?utm_source=OGB&pli=1', inf_un)


    Hp_four      = add_fournisseur(compagnie="HP",
    phone="97164538463",
    email="hp@hp.com",
    address="HP Houston")

    ec_hp_prod = add_materiel(lib="Ecran HP",
    cat=equippcfixe_cat,
    desc= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="15000",
    qte="110",
    four=Hp_four)

    waffo_cons     = add_consultant(nom="Waffo",
    prenom="Luc",
    phone="699581262",
    email="waffoluc@gmail.com")


    progra_c_svc = add_service(nom="Programmation C",
    type=glo_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="50000",
    cons=waffo_cons)


    alan_and_steve  = add_client(societe="Ets Alan And Steve",
    prenom="Alain Ghiscar",
    nom= "Soupkoudjou",
    fonction="pousseur",
    phone="699127737",
    email="alan_and_steve@yahoo.fr",
    address="Cite Verte G31")







    print "Liste Des Donnes Dans la BD:"
    print "Liste Des BlogPost:"
    for bp in BlogPost.objects.all():
        print bp
    print "Liste Des CommentairesBlogPosts:"
    for cbp in CommentBlogPost.objects.all():
        print cbp
    print "Liste Des Likes BlogPost:"
    for lbp in LikeBlogPost.objects.all():
        print lbp
    print "Liste Des Like Commentaires BlogPost:"
    for lcbp in LikeCommentBlogPost.objects.all():
        print lcbp

    print "Liste Des Produits Par Categories"
    for c in CategoryMateriel.objects.all():
        for p in Materiel.objects.filter(category=c):
	        print "[+] Produit: {0} ( Category: {1} ) --".format(str(p), str(c))

    print "Liste Des Services Par Categories"
    for c in CategoryService.objects.all():
        for s in Service.objects.filter(category=c):
	        print "[+] Service: {0} ( Type: {1} ) --".format(str(s), str(c))

    # Fonctions de population individuelles.

def add_blog_post(title, content):
    bp = BlogPost.objects.get_or_create(titre=title, contenu=content)[0]
    return bp

def add_comment_bp(author, comm):
    cbp = CommentBlogPost.objects.get_or_create(autheur=author, commentaire=comm)
    return cbp


def add_like_blog_post(liker):
    lbp = LikeBlogPost.objects.get_or_create(autheur=liker)
    return lbp


def add_like_comm_bp(liker):
    lcbp = LikeCommentBlogPost.objects.get_or_create(autheur=liker)
    return lcbp


if __name__ == '__main__':
    print "[*] Starting WAFFO Population Script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','waffo.settings')
    from blog.models import BlogPost, BlogSection, SectionSection, LikeBlogPost, CommentBlogPost, LikeCommentBlogPost
    populate()
    print "[+] WAFFO DataBase Populated Successfully!!!"
