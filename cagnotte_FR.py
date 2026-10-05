#os permet d'aller chercher une information dans un fichier (nouvelle liste avec les cagnotte du créateur)
#json bibliothéque pour utiliser les fichiers
import os
import json
def verifint(x):
  verif=0
  while verif==0:
    if x.isalpha() :
      #vérifie si le x est une lettre
      x=input("erreur veuiller rentrer un nombre  ") 
    else:
      verif=1
      x=(int(x))
      return x
def menu1G():
  #Fonction du menu 
  print("""
  Bonjour,bienvenue sur les cagnottes en ligne que voulez vous faire ?
  """)
  x=input( '''
  Si vous voulez vous inscrire taper  :  1
  Si vous voulez vous connecter taper :  2
  Si vous êtes invité et que vous voulez participer a une cagnotte taper : 3
  Sortir du site taper : 4
  ''')
  x=verifint(x)
  while x > 4 or x < 1:
      print(
      "Merci de sélectionner le nombre entre 1 et 4 qui correspond à votre demande."
      )
      x =input("""
    Si vous voulez vous creer une cagnotte taper  :  1
    Si vous voulez vous supprimer une cagnotte taper :  2
    Si vous voulez vous annulé une cagnotte taper : 3
    Sortir du site taper : 4
      """)
      x=verifint(x)
  return x
def menu11(listinscription):
  #fonction de l'inscription
  print("Inscription : ")
  inscription = {
   "email": 0,
   "password": 0,
   "nom": 0,
   "prenom": 0,
   "femme/homme": 0,
   "age": 0,
   "nationalite": 0
  }
  em = input("""
  Quel est votre email ?
  """)
  ver = verificationemailexistant(em,listinscription)
  if ver == 1:
    pas = input("""
    Quel est votre mot de passe ?
    """)
    no = input("""
    Quel est votre nom ?
    """)
    pr = input("""
    Quel est votre prenom ?
    """)
    fh = input("""
    Etes vous une femme ou un homme ou neutre ?
    """)
    while fh != 'homme' and fh != 'femme' and fh != "neutre" :
      print("Vous devez répondre à la question par femme, homme ou neutre.")
      fh = input("""
      Etes vous une femme ou un homme ou neutre ?
      """)
      print("Vous êtes ", fh)
    na = input("""De quelle nationalité etes vous ?
    """)
    x = input("""
    Quel âge avez vous ?
    """)
    verifint(x)
    inscription["email"] = em
    inscription["password"] = pas
    inscription["nom"] = no
    inscription["prenom"] = pr
    inscription["femme/homme"] = fh
    inscription["age"] = x
    inscription["nationalite"] = na
    inscription["commentaire"] = 0
  
    # Ajoute dans la liste le dico inscription
    listinscription.append(inscription)  
def verificationemailexistant(em,listinscription):
  #Fonction vérification de l'eamil lors de l'inscription 
  for i in range(len(listinscription)):
    v = listinscription[i]["email"]
    if v == em:
      print("Nous avons deja un compte pour cette adresse mail")
      return 0
  return 1
def verificactionconection(listinscription):
  #Fonction de la vérification de la connexion 
  print("Connexion : ")
  em1 = 1
  pas = 1
  ve = 0
  we = 0
  compt=0
  while compt==0:
    indice=0
    em1 = input("""
    Quelle est votre adresse mail ? 
    """)
    pas = input("""
    Quel est votre mot de passe ? 
    """)
    for i in range(len(listinscription)):
      ve = listinscription[i]["email"]
      we = listinscription[i]["password"]
      if ve == em1 and we == pas:
        print("Vous êtes connecté")
        indice=1
        compt=1
        break
    if indice==0:
      print("Le mot de passe ou l'adresse email ne sont ne sont pas connues")
  return em1
def menu2G():
  #Fonction du menu de cagnotte
  x = input("""
  Si vous voulez creer une cagnotte taper  :  1
  Si vous voulez accéder à l'espace commentaire de cagnotte taper :  2
  Si vous voulez annulé une cagnotte taper : 3
  Si vous voulez supprimer une cagnotte taper : 4
  Si vous voulez modifier l'espace commentaire de votre compte taper :5
  Sortir du site taper : 6
  """)
  x=verifint(x)
  while x > 6 or x < 1:
    print(
     "Merci de sélectionner le nombre entre 1 et 4 qui correspond à votre demande."
    )
    x = input("""
  Si vous voulez creer une cagnotte taper  :  1
  Si vous voulez accéder à l'espace commentaire de cagnotte taper :  2
  Si vous voulez annulé une cagnotte taper : 3
  Si vous voulez supprimer une cagnotte taper : 4
  Si vous voulez modifier l'espace commentaire de votre compte taper :5
  Sortir du site taper : 6
  """)
    x=verifint(x)
  return x
def menu21(listinscription,listcagnotte,email):
  #Fonction de la création d'une cagnotte
  cagnotte = {
   "emailcreateur":0,
   "nomdelaC": 0,
   "datedelaC": 0,
   "evenedelaC": 0,
   "cadenv": 0,
   "tplbroufx": 0,
   "tpanoouan": 0,
   "nomp": 0,
   "montant": 0}
  #permet de récupérer l'email du créateur grâce à la fonction verificationconnection()
  emailcreateur=email
  ca = input("""
  Comment voulez vous nommer votre cagnotte ?
  """)
  ver = verificationnomcagnotteexistant(ca,listcagnotte)
  if ver == 1:
    print("Votre cagnotte s'appelle", ca)
    ttd = input("""
    Quel est la date de l'événement ?
    """)
    print("la date de votre événement est", ttd)
    tte = input("""
    Quel est l'évènement ? 
    """)
    print("Votre évènement est", tte)
    cad = input("""
    Quel est le cadeau enviseagé ?
    """)
    print("Le cadeau envisagé est ", cad)
    tp = input(
     """Quelle est le type de participation pour votre cagnotte : libre ou fixee ?
     """)
    while tp != 'libre' and tp != 'fixee':
      print("Vous devez répondre à la question par fixee ou libre.")
      tp = input(
       """Quelle est le type de participation pour votre cagnotte : libre ou fixee ?
       """
      )
    print("Votre cagnotte est ", tp)
    if tp == "fixee":
      montant = input("""
      A combien fixee vous la cagnotte ?
      """)
    else:
      montant = "montant libre"
    print("La participation à la cagnotte est ", montant)
    tpa = input(
     """
     Quelle est le type de participation pour votre cagnotte : nominative ou anonyme ?
     """)
    while tpa != 'nominative' and tpa != 'anonyme':
      print("Vous devez répondre par nominative ou anonyme.")
      tpa = input(
       """
       Quelle est le type de participation pour votre cagnotte : nominative ou anonyme ?
       """)
    print("Votre cagnotte est ", tpa)
    mails = participant()
    print('Les mails des participants à la cagnotte sont ', mails)
  
    cagnotte["emailcreateur"] = emailcreateur
    cagnotte["nomdelaC"] = ca
    cagnotte["datedelaC"] = ttd
    cagnotte["evenedelaC"] = tte
    cagnotte["cadenv"] = cad
    cagnotte["tplbroufx"] = tp
    cagnotte["tpanoouan"] = tpa
    cagnotte["nomp"] = mails
    cagnotte["montant"] = 0
    cagnotte["commentaire"] = 0
    # Ajoute dans la liste le dico cagnotte
    listcagnotte.append(cagnotte) 
def verificationnomcagnotteexistant(ca,listcagnotte):
  #Fonction vérification que le nom de le cagnotte n'existe pas
  for i in range(len(listcagnotte)):
    v = listcagnotte[i]["nomdelaC"]
    if v == ca:
      print("Ce nom de cagnotte existe déjà, veuillez la renomer")
      return 0
  return 1
def participant():
  #Fonction qui donne la liste des mails des participants et leurs cagnotte
  x=input("""
  Entrer le nombre de participants
  """)
  x=verifint(x)
  listparticipant=[]*x
  for i in range (x):
    mailpart=input("""
    Entrer le mail
    """)
    while mailpart in listparticipant:
      print("Ce mail existe déjà")
      mailpart=input("""
      Entrer le mail
      """)
    listparticipant.append(mailpart)
  return listparticipant
def montant(numlis,listcagnotte):
  #Fonction qui ajoute les montants des participants dans leurs cagnotte associé 
  montant=input("""
  Entrer le montant a mettre sur la cagnotte
  """)

  ancienmontant= listcagnotte[numlis]['montant']
  calculmontant= (int(ancienmontant)+(int(montant)))
  # Ajoute dans la liste le dico inscription
  listcagnotte[numlis]['montant'] = calculmontant
def participationcagnotte(listcagnotte):
  #Fonction qui a un invité de participer à une cagnotte
  em = 0
  x=0
  ve = 1
  verif=0
  while verif==0:
    verif2=0
    em = input("Quelle est votre adresse mail ?  " )
    while em == "":
      print("rentrer une valeur pour l'adresse mail  ")
      em = input("Quelle est votre adresse mail ?  " )
    pas = input("si vous avez oublié votre email, taper oubli pour faire retour  " )
    if pas=='oubli':
      verif=1
      verif2=1
    while verif2==0:
      for i in range(len(listcagnotte)):
        ve = listcagnotte[i]["nomp"]
        if em in ve:
          print(listcagnotte[i])
          x=input("""
          Si c'est la cagnotte sur laquelle vous voulez rajouter de l'argent sur la 
          cagnotte alors tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2 
          Pour faire retour tapez 3
          """)
          x=verifint(x)
          while x > 3 or x < 1:
            print("""Merci de sélectionner le nombre entre 1 et 3 qui correspond à votre demande.""")
            x=input("""
            Si c'est la cagnotte sur laquelle vous voulez rajouter de l'argent sur la 
            cagnotte alors tapez 1
            Si vous voulez passer a la cagnotte suivante tapez 2
            Pour faire retour tapez 3
            """)
            x=verifint(x)
          if x==1:
            print("Vous êtes connecté sur la cagnotte ",listcagnotte[i]["nomdelaC"])
            numlis=i
            montant(numlis,listcagnotte)
            verif=1
            verif2=1
            break
          if x==3:
            verif=1
            verif2=1
            break
      if x!=2:
        verif2=1
def comcagnotte(listcagnotte,email):
  ve = 1
  verif=0
  while verif==0:
    for i in range(len(listcagnotte)):
      ve = listcagnotte[i]["emailcreateur"]
      if email == ve:
        print(listcagnotte[i])
        x=input("""
        Si c'est la cagnotte à laquelle vous voulez rajouter un commentaire alors taper 1
        Pour passer à la cagnotte suivante taper 2
        Pour faire retour taper 3 
        """)
        x=verifint(x)
        while x > 3 or x < 1:
          print("""Merci de sélectionner le nombre entre 1 et 3 qui correspond à votre demande.""")
          x=input("""
          Si c'est la cagnotte sur laquelle vous voulez rajouter de l'argent sur la 
          cagnotte alors tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2
          Pour faire retour tapez 3
          """)
          x=verifint(x)
        if x==1:
          choixcom=input("""
          Si vous voulez ajouter un commentaire taper 1
          Si vous voulez remplacer un commentaire taper 2
          Si vous voulez supprimer les commentaire taper 3 
          Si vous voulez sortir taper sur 4
          """)
          while choixcom!='1' and choixcom!='2' and choixcom!='3' and choixcom!='4' :
            print("erreur taper 1,2,3 ou 4")
            choixcom=input("""
          Si vous voulez ajouter un commentaire taper 1
          Si vous voulez remplacer un commentaire taper 2
          Si vous voulez supprimer les commentaire taper 3 
          Si vous voulez sortir taper sur 4
          """)
          if choixcom=="1":
            #ajout du commentaire dans le dictionnaire choisis
            com=input("""
            entrer votre commentaire  
            """)
            anciencom= listcagnotte[i]['commentaire']
            listcom=[]
            listcom.append(com)
            listcom.append(anciencom)
            listcagnotte[i]['commentaire'] = listcom
            print(email,"a ajouté un commentaire dans la cagnotte",i+1)
          if choixcom=="2":
            #remplacement du commentaire dans le dictionnaire choisis
            com=input("""
            entrez votre commentaire  
            """)
            listcagnotte[i]["commentaire"]=com
            print(email," a remplacé un commentaire dans la cagnotte ",i+1)
          if choixcom=="3":
            #suppression des commentaires
            listcagnotte[i]["commentaire"]=0
            print(email,"a supprimé le(s) commentaire(s) dans la cagnotte",i+1)
          verif=1
          break
        if x==3:
          verif=1
def annulcagnotte(listcagnotteannule,listcagnotte,email):
  ve = 1
  verif=0
  transfertcagnotte=0
  while verif==0:
    for i in range(len(listcagnotte)):
      ve = listcagnotte[i]["emailcreateur"]
      if email == ve:
        print(listcagnotte[i])
        bonnecagnotte=input("""
          Si c'est la cagnotte que vous voulez annuler tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2
          Pour faire retour tapez 3
          """)
        while bonnecagnotte!='1' and bonnecagnotte!='2' and bonnecagnotte!='3' :
          print("erreur taper 1 ou 2")
          bonnecagnotte=input("""
          Si c'est la cagnotte que vous voulez annuler tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2
          Pour faire retour tapez 3
          """)
        if bonnecagnotte=='1':
          transfertcagnotte=listcagnotte[i]
          listcagnotte[i]["montant"]=0
          # Ajoute dans la listecagnotteannule le dico de la cagnotte correspondante
          listcagnotteannule.append(transfertcagnotte)
          listcagnotte.pop(i)
          print("Cagnotte",i+1,"est annulée")
          verif=1
          break    
        if bonnecagnotte=='3':
          verif=1
          break
def suppcagnotte(listcagnotte,email):
  ve = 1
  verif=0
  while verif==0:    
    for i in range(len(listcagnotte)):
      ve = listcagnotte[i]["emailcreateur"]
      if email == ve:
        print(listcagnotte[i])
        bonnecagnotte=input("""
          Si c'est la cagnotte que vous voulez supprimer tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2
          Pour faire retour tapez 3
          """)
        while bonnecagnotte!='1' and bonnecagnotte!='2' and bonnecagnotte!='3' :
          print("erreur taper 1 ou 2")
          bonnecagnotte=input("""
          Si c'est la cagnotte que vous voulez supprimer tapez 1
          Si vous voulez passer a la cagnotte suivante tapez 2
          Pour faire retour tapez 3
          """)
        if bonnecagnotte=='1':
          #retire la valeur de montant, qui correspond à l'argent de la cagnotte
          listcagnotte[i]["montant"]=0
          verif=1
          print("cagnotte",i+1,"est supprimée")
          break
        if bonnecagnotte=='3':
          verif=1
          break
def comdonnees(listinscription,email):
  ve = 1
  verif=0
  while verif==0:
      for i in range(len(listinscription)):
        ve = listinscription[i]["email"]
        if email == ve:
          print("commentaire : ", listinscription[i]["commentaire"])
          choixcom=input("""
          Si vous voulez ajouter un commentaire taper 1
          Si vous voulez remplacer un commentaire taper 2
          Si vous voulez supprimer les commentaire taper 3 
          Si vous voulez sortir taper sur 4
          """)
          while choixcom!='1' and choixcom!='2' and choixcom!='3' and choixcom!='4' :
            print("erreur taper 1,2,3 ou 4")
            choixcom=input("""
          Si vous voulez ajouter un commentaire taper 1
          Si vous voulez remplacer un commentaire taper 2
          Si vous voulez supprimer les commentaire taper 3 
          Si vous voulez sortir taper sur 4
          """)
          if choixcom=="1":
            #ajout du commentaire dans le dictionnaire choisis
            com=input("""
            Entre votre commentaire  
            """)
            anciencom= listinscription[i]['commentaire']
            listcom=[]
            listcom.append(com)
            listcom.append(anciencom)
            listinscription[i]['commentaire'] = listcom
            print(email," s'est ajouté un commentaire ")
          if choixcom=="2":
            #remplacement du commentaire dans le dictionnaire choisis
            com=input("""
            Entre votre commentaire  
            """)
            listinscription[i]["commentaire"]=com
            print(email," a remplacé son commentaire")
          if choixcom=="3":
            #suppression des commentaires
            listinscription[i]["commentaire"]=0
            print(email,"a supprimé son commentaire")
          verif=1
          break
  
  #PROGRAMME GENERAL
menu = 0
menu2 = 0
données=0
fichcagnotte=0
fichcagnotteannule=0
listinscription = []
listcagnotte = []
listcagnotteannule = []

données = open("donnees.json", "a")
if (os.path.getsize("donnees.json") == 0):
    json.dump(listinscription, données)
données.close()

with open("donnees.json","r") as f:    
  #lie la liste au fichier
  listinscription= json.load(f)
  
#ouvre le fichier cagnotte et initialisation d'un tab pour le fichier cagnotte
cagnotte = open("cagnotte.json", "a")
# Check la taille du fichier et créer une liste vide si le fichier est vide
if (os.path.getsize("cagnotte.json") == 0):
  json.dump(listcagnotte, cagnotte)
cagnotte.close()
with open("cagnotte.json","r") as f:
  #lie la liste au fichier
  listcagnotte= json.load(f) 

cagnotteannule = open("cagnotteannule.json", "a")
if (os.path.getsize("cagnotteannule.json") == 0):
  json.dump(listcagnotteannule, cagnotteannule)
cagnotteannule.close()
with open("cagnotteannule.json","r") as f:    
  #lie la liste au fichier
  listcagnotteannule= json.load(f)  

while menu != 4:
  menu=menu1G()
  if menu == 1:
    menu11(listinscription)
  if menu == 2:
    email=verificactionconection(listinscription)
    verifmenu2=0
    while verifmenu2==0:
      menu2=menu2G()
      if menu2 == 1:
        menu21(listinscription,listcagnotte,email)
      if menu2 == 2:
        print("Vous êtes dans l'espace commentaire de cagnotte.")
        comcagnotte(listcagnotte,email)
      if menu2 == 3:
        print("Vous êtes dans l'espace pour annuler une cagnotte.")
        annulcagnotte(listcagnotteannule,listcagnotte,email)
      if menu2 == 4:
        print("Vous êtes dans l'espace pour supprimer une cagnotte")
        suppcagnotte(listcagnotte,email)
      if menu2 == 5:
        print("Vous êtes dans l'espace commentaire de votre profil")
        comdonnees(listinscription,email)
      if menu2 == 6:
        verifmenu2=1
        print("retourner au menu 1")
  if menu == 3:
    print("Participation a une cagnotte")
    participationcagnotte(listcagnotte)
  if menu == 4:
    print("Vous êtes sorti du site.")
    
    with open("donnees.json","w") as f:
      # Ecrit dans le json la nouvelle liste
      json.dump(listinscription, f, indent=3, separators=(',', ': '))
    
    with open("cagnotte.json","w") as f:
      # Ecrit dans le json la nouvelle liste
      json.dump(listcagnotte, f, indent=3, separators=(',', ': '))
    
    with open("cagnotteannule.json","w") as f:
      # Ecrit dans le json la nouvelle liste
      json.dump(listcagnotteannule, f, indent=3, separators=(',', ': '))    