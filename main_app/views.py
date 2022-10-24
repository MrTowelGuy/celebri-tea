from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>okUUURRR</h1>')

def about(request):
    return render(request, 'about.html')


# Add new view
def tea_index(request):
  return render(request, 'tea/index.html', { 'tea': tea })



# Add the Cat class & list and view function below the imports
class Tea:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, type, description, witnesses):
    self.title = title
    self.type = type
    self.description = description
    self.witnesses = witnesses

tea = [
  Tea('Elon public intoxication', 'embarassing', 'A disoriented Elon Musk was sited in Helen Ga tripping on peyote. Eye witnesses have reported that he was in nothing but an adventure time bathrobe and a batman mask. He was apparently seen trying to administer cpr to a dead goldfish and crying his stupid little eyes out like a loser.', 7),
  Tea('Mickey Mouse Adultry House', 'adultry', 'Minnie, walking into her house with the camera crew from cheaters, found Mickey naked in the pantry with Courtney Love. Sources say that Mickey was somehow responsible for Courtney Love thinking that it was okay for her to make music.',10),
  Tea('Living inCyde', 'Unexpected', 'Leaked emails spill content showing that the frontman of Living in Fear, Curtis, had been emailing the members of crunk-core group BrokeNcyde to express his passion and love for their band. When said emails leaked BC-13 came on record to say that they wanted to set up a tour with them and Living in Fear. Curtis has since denied all allegations of writing such an email, saying that "BrokeNcyde is straight dog water ass clown music". Recent chilling updates had eye witnesses seeing Curtis listening to Bree Bree on their spotify friend activity, Curtis forgetting to put his spotify on a private listening session.', 4569)
]
