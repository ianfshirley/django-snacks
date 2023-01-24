from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/95/Nachos.2.jpg",
                "title": "Nachos",
                "description": "Nachos are a Mexican culinary dish consisting of fried tortilla chips or totopos covered with melted cheese or cheese sauce, as well as a variety of other toppings and garnishes, often including meats (such as ground beef or grilled chicken), vegetables (such as chili peppers, lettuce, tomatoes, and olives), and condiments such as salsa, guacamole, or sour cream.",
                "reference_url": "https://en.wikipedia.org/wiki/Nachos"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Noodlecat_-_Lee_Anne_Wong_-_%22Lucky_Dumpring_Jiao_Zi%22_%286739677033%29.jpg",
                "title": "Dumplings",
                "description": "Jiaozi (Chinese: 餃子; [tɕjàʊ.tsɨ] (listen); pinyin: jiǎozi) are Chinese dumplings commonly eaten in China and other parts of East Asia. Jiaozi are folded to resemble Chinese sycee and have great cultural significance attached to them within China. Jiaozi are one of the major dishes eaten during the Chinese New Year throughout Northern China and eaten all year round in the northern provinces.",
                "reference_url": "https://en.wikipedia.org/wiki/Jiaozi"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Buffalo_wings-01.jpg",
                "title": "Buffalo Wings",
                "description": "A Buffalo wing in American cuisine is an unbreaded chicken wing section (flat or drumette) that is generally deep-fried and then coated or dipped in a sauce consisting of a vinegar-based cayenne pepper hot sauce and melted butter prior to serving.",
                "reference_url": "https://en.wikipedia.org/wiki/Buffalo_wing"
            },
        ]

        return context

class AboutView(TemplateView):
  template_name = 'about.html'
