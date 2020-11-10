#De la librería behave, importame todo
from behave import *
#Importamos de la librería selenium, webdriver
from selenium import webdriver
#Importamos de la librería nose sus herramientas y podemos
#determinar el tipo de assert que vamos a utilizar
from nose.tools import assert_equal


#Ahora vamos a definir todos los steps que tenemos:
#Agregamos el decorador correspondiente
#Given, es la precondición.
@given('the user is in the Main Page')
#Le vamos a pasar a la función el parámetro context
def step_impl(context):
    #driver = webdriver.Chrome('./drivers/chromedriver.exe')

    #Considerar, driver solo existe en esta función, es su alcance (scope).
    #No se puede utilizar self.driver porque no estamos en una clase.
    #La solución es, compartir datos entre steps, así sea el webdriver
    #datos que se van a ir pasando porque los van requeriendo
    #En este caso, por algo estoy pasando la variable/parámetro context
    #en todas las funciones que uso, voy a tener un contexto, al cual le voy
    #a agregar todas la variables, que yo tenga ganas de meterle a mi código.

    context.browser = webdriver.Chrome('./drivers/chromedriver.exe')
    context.browser.implicitly_wait(8)
    context.browser.get('http://automationpractice.com/index.php')


@when('the user clicks on Dresses Button')
#Le vamos a pasar a la función el parámetro context
def step_impl(context):
    #Ahora puedo usar el context.browser
    #en cualquier función que tenga.
    context.browser.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a').click()

@then('the user should see Dresses Page')
#Le vamos a pasar a la función el parámetro context
def step_impl(context):
    #En los then, tiene que haber un assert, porque acá se realizan las
    #verificaciones. Tenemos un problemita, porque la librería unittest, nos
    #va a quedar un poco incomodo de implementar.
    #Por tal motivo, vamos a usar una parte de una nueva librería llamada
    #Nose, que va a ser mas fácil de usar.
    #Vamos a dar un tiempo para que cargue la página con sus elementos.
    #Por tanto, agregamos un implicit wait en el @given.
    #Agregamos un espacio a nuestro texto que agregamos para que se compare context
    #el texto que trae el test; 'DRESSES '' == 'DRESSES '
    assert_equal(context.browser.find_element_by_class_name('cat-name').text, 'DRESSES ')
