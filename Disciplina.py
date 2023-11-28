
class Disciplina():
    def __init__(self,disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion):
        self.disciplina_id = disciplina_id
        self.gran_area_codigo = gran_area_codigo
        self.gran_area_descripcion = gran_area_descripcion
        self.area_codigo = area_codigo
        self.area_descripcion = area_descripcion
        self.disciplina_codiga = disciplina_codigo
        self.disciplina_descripcion = disciplina_descripcion
        
    def __str__(self):
        return ('El id de esta disciplina es {}, el gran area {}, el area {} y la descripcion {}'.format(self.disciplina_id, self.gran_area_descripcion, self.area_descripcion, self.disciplina_descripcion))