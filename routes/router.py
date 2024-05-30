from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from flask_cors import CORS
from controls.tda.stack.stack import Stack
from controls.calculadoraDaoControl import CalculadoraDaoControl
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito

@router.route('/')
def home():
    return render_template('pagina_inicio.html')



# RENDERS A LOS TEMPLATES
@router.route('/personas')
def ver_personas():
    cl = CalculadoraDaoControl()
    return render_template('nene/lista.html', lista=cl.to_dict())



@router.route('/personas/formulario')
def ver_guardar():
    return render_template('nene/guardar.html')



@router.route('/personas/guardar', methods=['POST'])
def guardar_personas():
    cl =  CalculadoraDaoControl()
    pila = Stack(10)
    data = request.form
    
    print("-----------------------------------")

    cl._calculadora._expresion = data['expresion']

    cl.calcular_expresion()
    return redirect('/personas', code=302)




@router.route('/personas/eliminar', methods=["POST"])
def eliminar_personas():
    cl = CalculadoraDaoControl()
    
    pos = request.form["id"]

    cl._delete(int(pos))
    return redirect("/personas", code=302)


