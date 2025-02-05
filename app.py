from flask import Flask, request, render_template
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import base64
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage
import shutil

app = Flask(__name__)
''' UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
 '''
def convertir_base64_a_pdf(base64_data_list, output_file, captura_pantalla=None):
    c = canvas.Canvas(output_file, pagesize=letter)
    first_image_drawn = False

    if captura_pantalla:
        
        if captura_pantalla.startswith("data:image/png;base64,"):
            captura_pantalla_data = captura_pantalla.split(",")[1]  
            try:
                captura_pantalla_image = ImageReader(BytesIO(base64.b64decode(captura_pantalla_data)))
                
                c.drawImage(captura_pantalla_image, 0, 0, width=letter[0], height=letter[1])
                first_image_drawn = True
            except base64.binascii.Error:
                print("Error: La cadena base64 de la captura de pantalla es inválida")
    
    for base64_data in base64_data_list:
        if base64_data.startswith("data:image/png;base64,"):
            image_data = base64_data.split(",")[1] 
            try:
                image = ImageReader(BytesIO(base64.b64decode(image_data)))
                if not first_image_drawn:
                    first_image_drawn = True
                else:
                    c.showPage() 
                c.drawImage(image, 0, 0, width=letter[0], height=letter[1])
            except base64.binascii.Error:
                print("Error: La cadena base64 de una imagen es inválida")

    c.save()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responsiva')
def responsiva():
    return render_template('responsiva.html')

@app.route('/responsiva', methods=['POST'])
def procesar_formulario_dos():
    tipodos = request.form['tipodos']
    nombre = request.form['nombre']
    apellido_materno = request.form['apellido_materno']
    apellido_paterno = request.form['apellido_paterno']
    mail = request.form['mail']
    tipo = request.form['tipo']
    marca = request.form['marca']
    modelo = request.form['modelo']
    serie = request.form['serie']
    dispositivo = request.form['dispositivo']
    procesador = request.form['procesador']
    ram = request.form['ram']
    rom = request.form['rom']
    so = request.form['so']
    noinventario = request.form['noinventario']

    month_spanish = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                     'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    now = datetime.now()
    day = now.day
    monthdos = now.month
    month = month_spanish[monthdos - 1]
    year = now.year

    if tipodos != "":
        return render_template('documentoresponsiva.html', tipodos=tipodos, nombre=nombre, apellido_materno=apellido_materno, apellido_paterno=apellido_paterno, mail=mail, tipo=tipo, marca=marca, modelo=modelo, serie=serie, procesador=procesador, ram=ram, rom=rom, so=so, dispositivo=dispositivo, day=day, month=month, year=year, noinventario=noinventario)
    else:
        return render_template('error.html', message='Tipo de dispositivo no válido')


@app.route('/entrega')
def entrega():
    return render_template('entrega.html') 

@app.route('/entrega', methods=['POST'])
def procesar_formulario():
    tipodos = request.form['tipodos']
    nombre = request.form['nombre']
    apellido_materno = request.form['apellido_materno']
    apellido_paterno = request.form['apellido_paterno']
    mail = request.form['mail']
    marca = request.form['marca']
    modelo = request.form['modelo']
    serie = request.form['serie']
    procesador = request.form['procesador']
    ram = request.form['ram']
    rom = request.form['rom']
    so = request.form['so']
    cargador = request.form['cargador']
    bateria = request.form['bateria']
    dispositivio = request.form['dispositivo']
    observaciones = request.form['observaciones']
    observacionesDos = request.form['observacionesDos']
    noinventario = request.form['noinventario']

    month_spanish = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                     'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    now = datetime.now()
    day = now.day
    monthdos = now.month
    month = month_spanish[monthdos - 1]
    year = now.year

    if tipodos != "":
        return render_template('documentoentrega.html', tipodos=tipodos, nombre=nombre, apellido_materno=apellido_materno, apellido_paterno=apellido_paterno, marca=marca, modelo=modelo, serie=serie, procesador=procesador, ram=ram, rom=rom, cargador=cargador, bateria=bateria, observaciones=observaciones, observacionesdos=observacionesDos, day=day, month=month, year=year, mail=mail, noinventario=noinventario)
    else:
        return render_template('error.html', message='Tipo de dispositivo no válido')


@app.route('/guardar_imagen', methods=['POST'])
def guardar_imagen():
    data = request.get_json()
    imagenes_base64 = data.get('imagenes_base64')
    captura_pantalla = data.get('captura_pantalla')
    mail = data.get('mail')
    tipodos = data.get('tipodos')
    nombre = data.get('nombre')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    tipo_doc = "Entrega"
    
    imagenes_base64_con_prefijo = ["data:image/png;base64," + imagen_base64 for imagen_base64 in imagenes_base64]

    output_file = "output.pdf"
    convertir_base64_a_pdf(imagenes_base64_con_prefijo, output_file, captura_pantalla)

    enviar_pdf_por_correo(output_file, mail, tipodos, nombre, apellido_paterno, apellido_materno,tipo_doc)
    return 'PDF generado con éxito: {}'.format(output_file)


@app.route('/guardar_imagen_dos', methods=['POST'])
def guardar_imagen_dos():
    data = request.get_json()
    imagenes_base64 = data.get('imagenes_base64')
    captura_pantalla = data.get('captura_pantalla')
    mail = data.get('mail')
    tipodos = data.get('tipodos')
    nombre = data.get('nombre')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    tipo_doc = "Responsiva"
    
    imagenes_base64_con_prefijo = ["data:image/png;base64," + imagen_base64 for imagen_base64 in imagenes_base64]

    output_file = "output.pdf"
    convertir_base64_a_pdf(imagenes_base64_con_prefijo, output_file, captura_pantalla)

    enviar_pdf_por_correo(output_file, mail, tipodos, nombre, apellido_paterno, apellido_materno, tipo_doc)
    return 'PDF generado con éxito: {}'.format(output_file)


def enviar_pdf_por_correo(pdf_file, mail, tipodos, nombre, apellido_paterno, apellido_materno, tipo_doc):
    email_sender = "sysadmin@nave.mx"  
    password = "smiu cwfs pncw ovzp"  

    email_recipient = mail   

    subject = tipo_doc.upper() + " del dispositivo " + tipodos

    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = subject
    msg.set_content(f"Estimado/a {nombre.upper()} {apellido_paterno.upper()} {apellido_materno.upper()},\n\nEspero este correo le encuentre bien. Adjunto a este mensaje, encontrará la {tipo_doc.upper()} correspondiente al dispositivo {tipodos}. Le agradecería revisara el documento adjunto.\n\nQuedo a su disposición para cualquier consulta o aclaración adicional.\n\nSaludos cordiales.")

    with open(pdf_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, password)
        smtp.send_message(msg)
 #       shutil.rmtree(UPLOAD_FOLDER)
    print("Correo electrónico enviado con éxito")


if __name__ == '__main__':
    app.run(debug=True)


