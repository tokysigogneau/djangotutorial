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
