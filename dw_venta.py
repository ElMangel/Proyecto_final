DDL_QUERY =  '''
CREATE TABLE venta(
    idventa int primary key,
    fecha date,
    idcliente	int,
    idusuario int,
    idarticulo int,
    idcategoria	int,
    tipo_comprobante	varchar(20),
    serie_comprobante	varchar(7),
    num_comprobante	varchar(10),
    impuesto	decimal(4,2),
    total decimal(11,2),
    cantidad	int,
    precio	decimal(11,2),
    descuento	decimal(11,2),
    
    foreign key (idcliente) references cliente(idcliente),
    foreign key (idusuario) references usuario(idusuario),
    foreign key (idarticulo) references articulo(idarticulo),
    foreign key (idcategoria) references categoria(idcategoria)
)

CREATE TABLE cliente(
    idcliente int primary key,
    tipo_persona	varchar(20),
    nombre	varchar(100),
    tipo_documento	varchar(20),
    num_documento	varchar(20),
    direccion	varchar(70),
    telefono	varchar(20),
    email	varchar(50)
)

CREATE TABLE usuario(
	idusuario	int primary key,
    nombre	varchar(100),
    tipo_documento	varchar(20),
    num_documento	varchar(20),
    direccion	varchar(70),
    telefono	varchar(20),
    email	varchar(50)  
)

CREATE TABLE articulo(
	idarticulo	int primary key,
    codigo varchar(50),
    nombre	varchar(100),
    precio_venta	decimal(11,2),
    stock	int
)
CREATE TABLE categoria(
	idcategoria	int primary key,
    nombre	varchar(50),
    descripcion	varchar(255),
    estado bit
)
'''