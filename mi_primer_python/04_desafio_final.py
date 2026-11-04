nombre_producto = 'pan';
precio_unitario = 250.0;
cantidad = 12;
disponiple = True;
dinero_cliente = 3000;
subtotal = precio_unitario * cantidad;
descuento = subtotal * 0.1;
total = subtotal - descuento;

print(f"""Nombre del producto: {nombre_producto}, Tipo de variable: {type(nombre_producto)}
Precio unitario: {precio_unitario}, Tipo de variable: {type(precio_unitario)}
Cantidad de compra: {cantidad}, Tipo de variable: {type(cantidad)}
Está disponible? {disponiple}, Tipo de variable: {type(disponiple)}
Dinero del cliente: {dinero_cliente}

Subtotal: {subtotal}
Descuento: {descuento}
Total a pagar: {total}
Dinero restante: {dinero_cliente - total}""")