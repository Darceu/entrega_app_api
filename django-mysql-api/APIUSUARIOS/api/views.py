
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

# Create your views here.


class UsuariosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_usuario=0):
        if (id > 0):
            usuario_i = list(Usuario.objects.filter(id_usuario=id).values())
            if len(usuario_i) > 0:
                usuario = usuario_i[0]
                datos = {'message': "Success", 'usuario': usuario}
            else:
                datos = {'message': "Usuario not found..."}
            return JsonResponse(datos)
        else:
            usuario_i = list(Usuario.objects.values())
            if len(usuario_i) > 0:
                datos = {'message': "Success", 'usuario': usuario_i}
            else:
                datos = {'message': "usuario not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Usuario.objects.create(id_usuario=jd['id'], correo=jd['correo'], contraseña=jd['contraseña'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id_usuario):
        jd = json.loads(request.body)
        usuario_i = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuario_i) > 0:
            usuario_i_id_usuario = Usuario.objects.get(id=id)
            usuario.correo = jd['correo']
            usuario.contraseña = jd['contraseña']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)

    def delete(self, request, id_usuario:
        usuario_i = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuario_i) > 0:
            Usuario.objects.filter(id_usuario=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)
