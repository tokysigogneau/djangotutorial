2.2.1.5 : il peut pas se connecter sans avoir le status equipe ou super utilisateur
2.2.1.7 : j'ai retiré son status equipe pour desactiver le compte sans supprimer

## Exercice Shell : 

### 2.2.2.2 Questions
#### 1 :
>>> for q in Question.objects.all() : print(q)
... 
What's up?
Qui gagne en 1v1 : Toto ou Tata?
Vous aimez le chocolat ?
Votre matière préférée ?
Quel âge avez vous?

#### 2 : 
>>> for q in Question.objects.all() : print(q.question_text); print (q.pub_date)
... 
What's up?
2026-02-23 12:32:12.577308+00:00
Qui gagne en 1v1 : Toto ou Tata?
2026-02-20 13:52:24+00:00
Vous aimez le chocolat ?
2026-02-10 14:03:04+00:00
Votre matière préférée ?
2026-02-19 14:07:08+00:00
Quel âge avez vous?
2026-02-13 14:07:30+00:00
>>> 
#### 3 : 
>>> q = Question.objects.get(pk=2)
>>> q
<Question: Qui gagne en 1v1 : Toto ou Tata?>

#### 4 : 

>>> for c in Choice.objects.all() : print(c.question); print (c.choice_text)    
... 
What's up?
Not much
What's up?
The sky
Qui gagne en 1v1 : Toto ou Tata?
Toto
Qui gagne en 1v1 : Toto ou Tata?
Tata
Vous aimez le chocolat ?
Bof
Vous aimez le chocolat ?
Pas mal
Vous aimez le chocolat ?
C'est bon
Vous aimez le chocolat ?
Oui !!
Votre matière préférée ?
Français
Votre matière préférée ?
Math
Votre matière préférée ?
Sport
Votre matière préférée ?
Musique
Quel âge avez vous?
0-12 ans
Quel âge avez vous?
13-17 ans
Quel âge avez vous?
18-25
Quel âge avez vous?
26-50
>>> 

#### 5 : 
>>> for c in Choice.objects.all() : print(c.question); print ("Choix : ", c.choice_text); print("Nb votes : " , c.votes) 
... 
What's up?
Choix :  Not much
Nb votes :  0
What's up?
Choix :  The sky
Nb votes :  0
Qui gagne en 1v1 : Toto ou Tata?
Choix :  Toto
Nb votes :  0
Qui gagne en 1v1 : Toto ou Tata?
Choix :  Tata
Nb votes :  0
Vous aimez le chocolat ?
Choix :  Bof
Nb votes :  0
Vous aimez le chocolat ?
Choix :  Pas mal
Nb votes :  0
Vous aimez le chocolat ?
Choix :  C'est bon
Nb votes :  0
Vous aimez le chocolat ?
Choix :  Oui !!
Nb votes :  0
Votre matière préférée ?
Choix :  Français
Nb votes :  0
Votre matière préférée ?
Choix :  Math
Nb votes :  0
Votre matière préférée ?
Choix :  Sport
Nb votes :  0
Votre matière préférée ?
Choix :  Musique
Nb votes :  0
Quel âge avez vous?
Choix :  0-12 ans
Nb votes :  0
Quel âge avez vous?
Choix :  13-17 ans
Nb votes :  0
Quel âge avez vous?
Choix :  18-25
Nb votes :  0
Quel âge avez vous?
Choix :  26-50
Nb votes :  0
>>> 
#### 7 : 
>>> for q in Question.objects.all().order_by("-pub_date"): print(q.question_text); print(q.pub_date);
... 
What's up?
2026-02-23 12:32:12.577308+00:00
Qui gagne en 1v1 : Toto ou Tata?
2026-02-20 13:52:24+00:00
Votre matière préférée ?
2026-02-19 14:07:08+00:00
Quel âge avez vous?
2026-02-13 14:07:30+00:00
Vous aimez le chocolat ?
2026-02-10 14:03:04+00:00
>>>
#### 9 : 
>>> from django.utils import timezone                                      
>>> q = Question(question_text="Sucré ou salé?", pub_date=timezone.now())
>>> q.save()
>>> q.id
6
#### 10 : 
>>> q.choice_set.create(choice_text="Sucré", votes=0)
<Choice: Sucré>
>>> q.choice_set.create(choice_text="Salé", votes=0) 
<Choice: Salé>
>>> q.save()

#### 11 : 
>>> for q in Question.objects.all():  
...     if Question.was_published_recently(q) :
...             print(q.question_text)         
... 
What's up?
Sucré ou salé?
>>> 
> 
## 2.2.3

### 1 :
>>> Question.age(q)
datetime.timedelta(seconds=86308, microseconds=518092)
>>> 
