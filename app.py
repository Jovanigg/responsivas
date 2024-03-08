from flask import Flask, render_template, request
from datetime import datetime
import calendar


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responsiva')
def responsiva():
    return render_template('responsiva.html')

@app.route('/responsiva', methods=['POST'])
def procesar_formulario_dos():
    tipodos = request.form['tipodos']
    ##########################################################################################################
    nombreComputo = request.form['nombreComputo']
    apellido_maternoComputo = request.form['apellido_maternoComputo']
    apellido_paternoComputo = request.form['apellido_paternoComputo']
    mailComputo = request.form['mailComputo']
    tipoComputo = request.form['tipoComputo']
    marcaComputo = request.form['marcaComputo']
    modeloComputo = request.form['modeloComputo']
    serieComputo = request.form['serieComputo']
    procesadorComputo = request.form['procesadorComputo']
    ramComputo = request.form['ramComputo']
    romComputo = request.form['romComputo']
    ##########################################################################################################
    nombreAuricular = request.form['nombreAuricular']
    apellido_maternoAuricular = request.form['apellido_maternoAuricular']
    apellido_paternoAuricular = request.form['apellido_paternoAuricular']
    mailAuricular = request.form['mailAuricular']
    tipoAuricular = request.form['tipoAuricular']
    marcaAuricular = request.form['marcaAuricular']
    modeloAuricular = request.form['modeloAuricular']
    serieAuricular = request.form['serieAuricular']
    ##########################################################################################################
    nombreDispositivoMovil = request.form['nombreDispositivoMovil']
    apellido_maternoDispositivoMovil = request.form['apellido_maternoDispositivoMovil']
    apellido_paternoDispositivoMovil = request.form['apellido_paternoDispositivoMovil']
    mailDispositivoMovil = request.form['mailDispositivoMovil']
    tipoDispositivoMovil = request.form['tipoDispositivoMovil']
    marcaDispositivoMovil = request.form['marcaDispositivoMovil']
    modeloDispositivoMovil = request.form['modeloDispositivoMovil']
    serieDispositivoMovil = request.form['serieDispositivoMovil']
    procesadorDispositivoMovil = request.form['procesadorDispositivoMovil']
    ramDispositivoMovil = request.form['ramDispositivoMovil']
    romDispositivoMovil = request.form['romDispositivoMovil']
    soDispositivoMovil = request.form['soDispositivoMovil']
    ##########################################################################################################
    nombreTablet = request.form['nombreTablet']
    apellido_maternoTablet = request.form['apellido_maternoTablet']
    apellido_paternoTablet = request.form['apellido_paternoTablet']
    mailTablet = request.form['mailTablet']
    tipoTablet = request.form['tipoTablet']
    marcaTablet = request.form['marcaTablet']
    modeloTablet = request.form['modeloTablet']
    serieTablet = request.form['serieTablet']
    procesadorTablet = request.form['procesadorTablet']
    ramTablet = request.form['ramTablet']
    romTablet = request.form['romTablet']
    soTablet = request.form['soTablet']
    ##########################################################################################################
    nombreTv = request.form['nombreTv']
    apellido_maternoTv = request.form['apellido_maternoTv']
    apellido_paternoTv = request.form['apellido_paternoTv']
    mailTv = request.form['mailTv']
    tipoTv = request.form['tipoTv']
    marcaTv = request.form['marcaTv']
    modeloTv = request.form['modeloTv']
    serieTv = request.form['serieTv']
    ##########################################################################################################
    nombreOtros = request.form['nombreOtros']
    apellido_maternoOtros = request.form['apellido_maternoOtros']
    apellido_paternoOtros = request.form['apellido_paternoOtros']
    mailOtros = request.form['mailOtros']
    tipoOtros = request.form['tipoOtros']
    dispositivoOtros = request.form['dispositivoOtros']
    marcaOtros = request.form['marcaOtros']
    modeloOtros = request.form['modeloOtros']
    serieOtros = request.form['serieOtros']

    month_spanish = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                     'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    now = datetime.now()
    day = now.day
    monthdos = now.month
    month = month_spanish[monthdos - 1]
    year = now.year

    if tipodos == "computo":
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreComputo, apellido_materno=apellido_maternoComputo, apellido_paterno=apellido_paternoComputo, mail=mailComputo, tipo=tipoComputo, marca=marcaComputo, modelo=modeloComputo, serie=serieComputo, procesador=procesadorComputo, ram=ramComputo, rom=romComputo, day=day, month=month, year=year)
    elif tipodos == "auricular":
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreAuricular, apellido_materno=apellido_maternoAuricular, apellido_paterno=apellido_paternoAuricular, mail=mailAuricular, tipo=tipoAuricular, marca=marcaAuricular, modelo=modeloAuricular, serie=serieAuricular, day=day, month=month, year=year)
    elif tipodos == "dispositivo_movil":
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreDispositivoMovil, apellido_materno=apellido_maternoDispositivoMovil, apellido_paterno=apellido_paternoDispositivoMovil, mail=mailDispositivoMovil, tipo=tipoDispositivoMovil, marca=marcaDispositivoMovil, modelo=modeloDispositivoMovil, serie=serieDispositivoMovil, procesador=procesadorDispositivoMovil, ram=ramDispositivoMovil, rom=romDispositivoMovil, so=soDispositivoMovil, day=day, month=month, year=year)
    elif tipodos == "tablet":
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreTablet, apellido_materno=apellido_maternoTablet, apellido_paterno=apellido_paternoTablet, mail=mailTablet, tipo=tipoTablet, marca=marcaTablet, modelo=modeloTablet, serie=serieTablet, procesador=procesadorTablet, ram=ramTablet, rom=romTablet, so=soTablet, day=day, month=month, year=year)
    elif tipodos == 'otros':
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreTv, apellido_materno=apellido_maternoTv, apellido_paterno=apellido_paternoTv, mail=mailTv, tipo=tipoTv, marca=marcaTv, modelo=modeloTv, serie=serieTv, day=day, month=month, year=year)
    elif tipodos == 'otros':
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombreOtros, apellido_materno=apellido_maternoOtros, apellido_paterno=apellido_paternoOtros, mail=mailOtros, tipo=tipoOtros, dispositivo=dispositivoOtros, marca=marcaOtros, modelo=modeloOtros, serie=serieOtros, day=day, month=month, year=year)
    else:
        return render_template('error.html', message='Tipo de dispositivo no válido')


@app.route('/entrega')
def entrega():
    return render_template('entrega.html') 


@app.route('/entrega', methods=['POST'])
def procesar_formulario():
    tipodos = request.form['tipodos']
    ##########################################################################################################
    nombreComputo = request.form['nombreComputo']
    apellido_maternoComputo = request.form['apellido_maternoComputo']
    apellido_paternoComputo = request.form['apellido_paternoComputo']
    marcaComputo = request.form['marcaComputo']
    mailComputo = request.form['mailComputo']
    modeloComputo = request.form['modeloComputo']
    serieComputo = request.form['serieComputo']
    procesadorComputo = request.form['procesadorComputo']
    ramComputo = request.form['ramComputo']
    romComputo = request.form['romComputo']
    cargadorComputo = request.form['cargadorComputo']
    bateriaComputo = request.form['bateriaComputo']
    observacionesComputo = request.form['observacionesComputo']
    ##########################################################################################################
    nombreAuricular = request.form['nombreAuricular']
    apellido_maternoAuricular = request.form['apellido_maternoAuricular']
    apellido_paternoAuricular = request.form['apellido_paternoAuricular']
    mailAuricular = request.form['mailAuricular']
    marcaAuricular = request.form['marcaAuricular']
    modeloAuricular = request.form['modeloAuricular']
    serieAuricular = request.form['serieAuricular']
    observacionesAuricular = request.form['observaciones_auricular']
    ##########################################################################################################
    nombreDispositivoMovil = request.form['nombreDispositivoMovil']
    apellido_maternoDispositivoMovil = request.form['apellido_maternoDispositivoMovil']
    apellido_paternoDispositivoMovil = request.form['apellido_paternoDispositivoMovil']
    mailDispositivoMovil = request.form['mailDispositivoMovil']
    marcaDispositivoMovil = request.form['marcaDispositivoMovil']
    modeloDispositivoMovil = request.form['modeloDispositivoMovil']
    serieDispositivoMovil = request.form['serieDispositivoMovil']
    procesadorDispositivoMovil = request.form['procesadorDispositivoMovil']
    ramDispositivoMovil = request.form['ramDispositivoMovil']
    romDispositivoMovil = request.form['romDispositivoMovil']
    soDispositivoMovil = request.form['soDispositivoMovil']
    observacionesDispositivoMovil = request.form['observacionesDispositivoMovil']
    ##########################################################################################################
    nombreTablet = request.form['nombreTablet']
    apellido_maternoTablet = request.form['apellido_maternoTablet']
    apellido_paternoTablet = request.form['apellido_paternoTablet']
    mailTablet = request.form['mailTablet']
    marcaTablet = request.form['marcaTablet']
    modeloTablet = request.form['modeloTablet']
    serieTablet = request.form['serieTablet']
    procesadorTablet = request.form['procesadorTablet']
    ramTablet = request.form['ramTablet']
    romTablet = request.form['romTablet']
    soTablet = request.form['soTablet']
    observacionesTablet = request.form['observacionesTablet']
    ##########################################################################################################
    nombreTv = request.form['nombreTv']
    apellido_maternoTv = request.form['apellido_maternoTv']
    apellido_paternoTv = request.form['apellido_paternoTv']
    marcaTv = request.form['marcaTv']
    modeloTv = request.form['modeloTv']
    mailTv = request.form['mailTv']
    serieTv = request.form['serieTv']
    observacionesTv = request.form['observacionesTv']
    ##########################################################################################################
    nombreOtros = request.form['nombreOtros']
    apellido_maternoOtros = request.form['apellido_maternoOtros']
    apellido_paternoOtros = request.form['apellido_paternoOtros']
    mailOtros = request.form['mailOtros']
    dispositivoOtros = request.form['dispositivoOtros']
    marcaOtros = request.form['marcaOtros']
    modeloOtros = request.form['modeloOtros']
    serieOtros = request.form['serieOtros']
    observacionesOtros = request.form['observacionesOtros']

    month_spanish = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                     'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    now = datetime.now()
    day = now.day
    monthdos = now.month
    month = month_spanish[monthdos - 1]
    year = now.year

    if tipodos == "computo":
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreComputo, apellido_materno=apellido_maternoComputo, apellido_paterno=apellido_paternoComputo, marca=marcaComputo, modelo=modeloComputo, serie=serieComputo, procesador=procesadorComputo, ram=ramComputo, rom=romComputo, cargador=cargadorComputo, bateria=bateriaComputo, observaciones=observacionesComputo, day=day, month=month, year=year, mail=mailComputo)
    elif tipodos == "auricular":
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreAuricular, apellido_materno=apellido_maternoAuricular, apellido_paterno=apellido_paternoAuricular, marca=marcaAuricular, modelo=modeloAuricular, serie=serieAuricular, observaciones=observacionesAuricular, day=day, month=month, year=year, mail=mailAuricular)
    elif tipodos == "dispositivo_movil":
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreDispositivoMovil, apellido_materno=apellido_maternoDispositivoMovil, apellido_paterno=apellido_paternoDispositivoMovil, marca=marcaDispositivoMovil, modelo=modeloDispositivoMovil, serie=serieDispositivoMovil, procesador=procesadorDispositivoMovil, ram=ramDispositivoMovil, rom=romDispositivoMovil, observaciones=observacionesDispositivoMovil, day=day, month=month, year=year, mail=mailDispositivoMovil, so=soDispositivoMovil)
    elif tipodos == "tablet":
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreTablet, apellido_materno=apellido_maternoTablet, apellido_paterno=apellido_paternoTablet, marca=marcaTablet, modelo=modeloTablet, serie=serieTablet, procesador=procesadorTablet, ram=ramTablet, rom=romTablet, so=soTablet, observaciones=observacionesTablet, day=day, month=month, year=year, mail=mailTablet)
    elif tipodos == 'tv':
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreTv, apellido_materno=apellido_maternoTv, apellido_paterno=apellido_paternoTv, marca=marcaTv, modelo=modeloTv, mail=mailTv, serie=serieTv, observaciones=observacionesTv, day=day, month=month, year=year)
    elif tipodos == 'otros':
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombreOtros, apellido_materno=apellido_maternoOtros, apellido_paterno=apellido_paternoOtros, marca=marcaOtros, modelo=modeloOtros, serie=serieOtros, observaciones=observacionesOtros, dispositivo=dispositivoOtros, day=day, month=month, year=year, mail=mailOtros)
    else:
        return render_template('error.html', message='Tipo de dispositivo no válido')




if __name__ == '__main__':
    app.run(debug=True)
