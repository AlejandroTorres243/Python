class Camiseta:

    # Definicion de sobrecarga del metodo init en la segunda parte
    #def __init__(self):
    #    self.marca = "Gucci"
    #    self.color = "Negro"
    #    self.precio = 100.00
    #    self.talla = "M"
    
    def __init__(self, marca, color, precio, talla):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.talla = talla
        self.comprobacionEnRebaja = False

    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - (self.precio*porcentaje)/100
        if(porcentaje < 100):
            self.comprobacionEnRebaja = True
    
    def infoProducto(self):
        info = f"Descripcion del producto \nMarca: {self.marca} \nCosto: {self.precio:.2f} \nColor: {self.color} \nTalla: {self.talla}\n"
        if(self.comprobacionEnRebaja):
            info += "ESTE PRODUCTO ESTA EN REBAJA \n #########################"
        return info

#camiseta = Camiseta()
#print(camiseta.marca)
#camiseta.aplicarDescuento(35)
#print(camiseta.precio)

camisetaNike = Camiseta("Nike", "Azul", 25.00, "L")
print(camisetaNike.marca)
camisetaNike.aplicarDescuento(45)
print(camisetaNike.precio)

