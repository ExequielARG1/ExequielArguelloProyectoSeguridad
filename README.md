#Exequiel_Arguello ProyectoSeguridad

LIBRERIAS UTILIZADAS;
PILLOW,
widget_tweaks



Este proyecto consiste en una aplicación web que permite a los usuarios  loguearse para poder acceder a la misma. Una vez logueado, el usuario puede crear, editar y eliminar sus propios posts, así como también ver los posts de otros usuarios.

Siendo un proyecto básico con una basta documentación se adapto para este proyecto de este curso.

El objetivo es darle comodidad a los empleados para poder modificar, crear, eliminar y ver los post de la empresa

Descripción de los models;
Personal:

Representa a los miembros individuales del personal o empleados.
nombre: Almacena el nombre del miembro del personal.
puesto: Indica el puesto o cargo que el miembro del personal ocupa.
descripcion: Proporciona una breve descripción o resumen sobre el miembro del personal.
foto: Contiene una imagen del miembro del personal. Si no se proporciona, se utilizará una imagen predeterminada.
La representación de cadena del modelo devuelve el nombre del miembro del personal.


Sucursal:

Representa las diferentes sucursales o localizaciones de una empresa u organización.
descripcion: Breve descripción de la sucursal.
horarios: Información sobre los horarios de atención o funcionamiento de la sucursal.
foto: Una imagen representativa de la sucursal. Usa una imagen predeterminada si no se proporciona.
ubicacion: Dirección o localización detallada de la sucursal.
La representación de cadena del modelo devuelve la descripcion de la sucursal.


AcercaDe:

Representa información sobre la empresa, organización o aplicación.
titulo: Título o encabezado de la sección o información.
descripcion: Descripción o contenido detallado relacionado con el título.
La representación de cadena del modelo devuelve el titulo.
CustomUser:

Extiende el modelo de usuario predeterminado de Django para incluir características personalizadas.
avatar: Una imagen de perfil para el usuario. Utiliza una imagen predeterminada si no se proporciona.
groups: Relación con los grupos a los que pertenece un usuario. Proporciona permisos basados en grupos.
user_permissions: Permisos específicos asociados al usuario.

Representa un formulario o registro de contacto.
name: Nombre de la persona que envía el mensaje.
email: Dirección de correo electrónico de la persona que envía el mensaje.
message: El contenido o cuerpo del mensaje enviado por la persona.


Cuenta administrativa;
username: admin
password: admin
