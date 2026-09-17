# Ejercicio 4

A partir de la vista: 

```py
def ejercicio4(request):
    usuarios = [
        {"nombre": "juan", "email": "juan@django"},
        {"nombre": "santi", "email": "juan@django"},
        {"nombre": "agustín", "email": "juan@django"},
    ]
    return render(request, "core/ejercicio4.html", {"usuarios": usuarios})
```

Crear el template `ejercicio4.html` e iterar sobre la lista y mostrar cada usuario.
