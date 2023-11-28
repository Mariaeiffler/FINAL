
class Estado_proyecto():
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        
    def __str__(self):
        return('El estado del proyecto es {}'.format(self.descripcion))