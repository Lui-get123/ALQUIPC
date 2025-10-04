from cx_Freeze import setup, Executable

# Dependencias que se incluirán
build_exe_options = {
    "packages": ["tkinter", "datetime", "random"],
    "include_files": [],
    "excludes": ["unittest", "pydoc", "doctest"]
}

# Configuración del ejecutable
setup(
    name="ALQUIPC Facturacion",
    version="1.0",
    description="Sistema de Facturacion ALQUIPC",
    options={"build_exe": build_exe_options},
    executables=[Executable("alquipc_facturacion.py", base="Win32GUI")]
)
