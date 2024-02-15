# Practicando POO
# Germán Fraga


class AuxVista:
    def __init__(
        self,
        var_dni,
        var_cuil,
        var_nombre,
        var_apellido,
        var_domicilio,
        var_fnacimiento,
        var_falta,
        var_art,
        var_obra,
        var_jornal,
        var_filtro,
        l_status,
        e_dni,
        e_cuil,
    ):
        self.var_dni = var_dni
        self.var_cuil = var_cuil
        self.var_nombre = var_nombre
        self.var_apellido = var_apellido
        self.var_domicilio = var_domicilio
        self.var_fnacimiento = var_fnacimiento
        self.var_falta = var_falta
        self.var_art = var_art
        self.var_obra = var_obra
        self.var_jornal = var_jornal
        self.var_filtro = var_filtro
        self.l_status = l_status
        self.e_dni = e_dni
        self.e_cuil = e_cuil

    # ***** MANIPULACION DE DATOS *****
    # ----- CREACION DE UNA LISTA PARA MOVIMIENTO DE LOS DATOS -----
    def create_list(self):
        data_list = [
            self.var_dni.get(),
            self.var_cuil.get(),
            self.var_nombre.get(),
            self.var_apellido.get(),
            self.var_domicilio.get(),
            self.var_fnacimiento.get(),
            self.var_falta.get(),
            self.var_obra.get().capitalize(),
            self.var_art.get(),
            self.var_jornal.get(),
        ]
        return data_list

    # ----- SETEO DE LOS ENTRY -----
    def set_entry(self, data_list: list):
        if data_list[0][1] != "-":
            self.var_dni.set(data_list[0][1])
            self.var_cuil.set(data_list[0][2])
            self.var_nombre.set(data_list[0][3])
            self.var_apellido.set(data_list[0][4])
            self.var_domicilio.set(data_list[0][5])
            self.var_fnacimiento.set(data_list[0][6])
            self.var_falta.set(data_list[0][7])
            self.var_obra.set(data_list[0][8])
            self.var_art.set(data_list[0][9])
            self.var_jornal.set(data_list[0][10])
            if not data_list[0][1]:
                self.l_status.config(text="Ok.", background="#B9F582")
                self.e_dni.config(state="normal")
                self.e_cuil.config(state="normal")
            else:
                self.l_status.config(
                    text="Puede modificar o dar de baja al registro.",
                    background="#B9F582",
                )
                self.e_dni.config(state="disabled")
                self.e_cuil.config(state="disabled")
