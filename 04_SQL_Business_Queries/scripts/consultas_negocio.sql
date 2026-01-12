-- ==========================================================
-- PROYECTO 04: ANÁLISIS DE NEGOCIO - TIENDA TECNOLÓGICA
-- ==========================================================

-- 1. VISTA GENERAL: Ver todos los productos disponibles
SELECT * FROM productos;

-- 2. ALERTAS DE INVENTARIO: Productos con stock menor a 20
SELECT nombre, stock 
FROM productos 
WHERE stock < 20;

-- 3. PRODUCTOS PREMIUM: El producto más caro con stock disponible
SELECT nombre, precio 
FROM productos 
WHERE stock >= 5 
ORDER BY precio DESC 
LIMIT 1;

-- 4. VALOR TOTAL: ¿Cuánto dinero hay invertido en bodega?
SELECT SUM(precio * stock) AS valor_total_bodega 
FROM productos;

-- 5. REABASTECIMIENTO: Productos económicos con mucho stock
SELECT nombre, stock, precio 
FROM productos 
WHERE precio < 100 AND stock > 50;

-- 6. ACTUALIZACIÓN DE PRECIOS: Incremento del 10% por inflación
UPDATE productos 
SET precio = precio * 1.10;

-- 7. LIMPIEZA DE CATÁLOGO: Eliminar productos descontinuados
DELETE FROM productos 
WHERE id_producto = 4;