
        

from unittest import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash

# browser = webdriver.Chrome()
# browser.get("http://127.0.0.1:8000/") 

# bu kod bize bu url ile bir browser acar.
## Bu normalde istenen birsey degildir. büyük projelerde, cloud da server ayaga kaldirir ve daha baska islerde yapar. Bunlar kapanmazsa maliyet olabilir. 
# o nedenle asagidaki ekilde yazariz. 

## önemli asagidaki test class i icinde yazdigimiz her birtest methodu test ile baslamalidir. 



            ### functional tests:

# class FunctionalTestCase(TestCase):
#         ## browser acma
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#         # isi bitince browser kapatma. buradaki func isimleri keyword
#     def tearDown(self):
#         self.browser.quit()

#         ## homepage de asagidaki yazi olup olmadigini test ediyoruz. 
#         # bu functional test
#     def test_there_is_homepage(self):
#         self.browser.get("http://127.0.0.1:8000/")
#         self.assertIn("Enter hash here", self.browser.page_source)  
#         ## assert : iddia etmek. icinde oldugunu iddia eder. 
#         ## iki parametre ister. birinci iddia ettigi sey, ikincisi gelen.
#         # eger iddia ettigi sey gelen ile ayni ise tamam.  


#         ## bu da functional test:
#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000/')
#         text = self.browser.find_element_by_id("id_text")
#         text.send_keys("hello")
#         self.browser.find_element_by_name("submit").click()
#         self.assertInHTML("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", self.browser.page_source)


## assertIn  python dan gelir.  assertInHtml ise django dan gelir. 



    ## teardown alternatif:

#  def tearDown(self) -> None:
#         return super().tearDown()



## functional test ler daha yavastir. cünkü browser calistirir. unit test ise cok daha hizlidir. 












        ## unit tests:

class UnitTestCase(TestCase):
        ### template test
        
    # def test_home_homepage_tempalte(self):
    #     # Go to the homepage
    #     response = self.client.get('/')
    #     # Search for home.html
    #     self.assertTemplateUsed(response, 'hashing/home.html')





        ### form test:

    def test_hash_form(self):
        # Check if there is a form, needs to filled with some data, for not to be an empty form which basically equals to False
        form = HashForm(data={'text': 'hello'})
        # Check if it is valid
        self.assertTrue(form.is_valid()) # burada fromun olup olmadigini kontrol ettik.

        # yani basarili ise formumuz var ve icine de veri ekleyebiliyoruz denir.






        #### view daki func imizi test:

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)







        ### model Test:

    def test_hash_object(self):
        # First create a hash object:  Hash modelinden bir object üretme
        hash = Hash()
        # the first property will be a sample text, and second will be the corresponding hash value of that text
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        # save new test properties to the db
        hash.save()
        # Get the object from db, django will search for this hash from the db, and bring us the object
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        # Check if the db value is equal to the true one
        ## db ye gönderdigimiz veri ile cektigimiz ayni mi onu test ediyoruz.
        self.assertEqual(hash.text,pulled_hash.text)

## onetoone yada many iliskinin testi icin diger tabloyu da import ederiz. bunlar arasinda iliski kurariz ve ona göre test ederiz. 








        ##### url test:  eger bu sayfada hello stringi görüyorsam dogru calisiyor. 

    def test_viewing_hash(self):
        # Inherit from Hash form:
        hash = Hash()
        # sample text will be 'hello' as always:
        hash.text = 'hello'
        # sample hash is the same as always
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        # save to the test db
        hash.save()
        # the url pattern should be as fallows, hash/<hash value>
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response,'hello')






















## soru oldugunda how to test model, django test forms gibi yazariz.

### python manage.py test -v 2 dersek cok daha detayli test yapar. 

## test drived development:  app i yapmadan önce test lerin olusturulmasi ve bu test ler üzerine kodlar yaziliyor. 

