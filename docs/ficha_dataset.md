# Ficha del Dataset - Comparación de Candidatos (U01.LAB02)

## 1. Formulación del Problema Seleccionado (Candidato Principal)
- **Dominio:** Finanzas / Riesgo de Crédito.
- **Unidad de análisis:** Un solicitante de crédito individual.
- **Decisión:** Evaluar si se aprueba o rechaza una solicitud crediticia mitigando la exposición al impago.
- **Target:** Riesgo crediticio (`credit_risk` o `class`: 1 = Buen riesgo / Pagador, 2 = Mal riesgo / Incumplidor).
- **Error más costoso:** Falso Negativo (clasificar a un cliente de mal riesgo como buen riesgo, otorgándole un crédito que no pagará y generando pérdida patrimonial directa).
- **Usuario de la solución:** Departamento de Riesgos y Analistas de Crédito de la entidad financiera.

---

## 2. Comparación de Candidatos

| Criterio | Candidato A: Statlog (German Credit Data) | Candidato B: Online Retail |
| :--- | :--- | :--- |
| **Procedencia** | UCI Machine Learning Repository (ID 144) | UCI Machine Learning Repository (ID 352) |
| **URL Documentación** | https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data | https://archive.ics.uci.edu/dataset/352/online+retail |
| **Licencia** | Creative Commons Attribution 4.0 (CC BY 4.0) | Creative Commons Attribution 4.0 (CC BY 4.0) |
| **Filas / Columnas** | 1,000 filas / 20 predictores + target | 541,909 filas / 8 atributos |
| **Target y Clases** | Binario natural (1 = Good, 2 = Bad) | No predefinido (requiere ingeniería de atributos previa) |
| **Ausentes** | 0 valores nulos directos | Presenta nulos en CustomerID y Description |
| **Riesgo de fuga** | Mínimo (variables del momento de la solicitud) | Alto si se agregan datos futuros de compra |
| **Decisión** | **Seleccionado como dataset de trabajo** | Descartado para modelado directo en esta unidad |


### Diccionario de Datos y Análisis de Fuga / Disponibilidad

| Variable | Significado | Unidad / Valores | Fuente | Momento de disponibilidad | Transformación prevista | Riesgo (Fuga / Sesgo) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`checking_status`** | Estado o saldo de la cuenta corriente del solicitante | Categórica ordinal (`<0 DM`, `0-200 DM`, `>=200 DM`, `sin cuenta`) | Formulario bancario / Buró | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Información histórica verificable antes de otorgar el crédito. |
| **`duration`** | Plazo solicitado para el crédito | Numérica discreta (Meses) | Solicitud formal de crédito | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Condición contractual pactada *a priori*. |
| **`credit_history`** | Historial de créditos y pagos previos | Categórica (`créditos críticos`, `al día`, `pagados con retraso`, etc.) | Buró de crédito interno/externo | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Comportamiento histórico anterior al trámite. |
| **`purpose`** | Propósito o destino del crédito | Categórica nominal (`auto nuevo`, `educación`, `muebles`, etc.) | Solicitud del cliente | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Motivo de la solicitud declarado al inicio. |
| **`credit_amount`** | Monto total del crédito solicitado | Numérica continua (Marcos alemanes / DM) | Solicitud formal de crédito | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Monto nominal evaluado previo a la aprobación. |
| **`savings_status`** | Saldo en cuentas de ahorro / depósitos | Categórica ordinal (`<100 DM`, `100-500 DM`, `>1000 DM`, etc.) | Estados de cuenta / Banco | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Patrimonio preexistente del solicitante. |
| **`employment`** | Tiempo en el empleo actual | Categórica ordinal (`desempleado`, `<1 año`, `1-4 años`, `>=7 años`) | Comprobante de ingresos / RRHH | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Antigüedad laboral verificada antes de aprobar. |
| **`installment_commitment`** | Tasa de cuota sobre el ingreso disponible | Numérica discreta (% del ingreso: 1, 2, 3, 4) | Cálculo sobre declaración de ingresos | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Razón financiera estimada *ex-ante*. |
| **`personal_status`** | Estado civil y sexo del solicitante | Categórica (`hombre soltero`, `mujer divorciada`, `hombre casado`, etc.) | Documento de identidad | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Riesgo ético/sesgo:** Variable sensible protegida. No presenta fuga, pero requiere vigilancia contra discriminación algorítmica. |
| **`other_parties`** | Existencia de codeudores o garantes | Categórica (`ninguno`, `co-solicitante`, `garante`) | Solicitud / Contrato crediticio | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Respaldo formal previo a la concesión. |
| **`residence_since`** | Años de residencia en el domicilio actual | Numérica discreta (Años: 1, 2, 3, 4) | Comprobante de domicilio | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Estabilidad residencial verificada al inicio. |
| **`property_magnitude`** | Bienes o propiedades de mayor valor | Categórica (`bienes raíces`, `seguro de vida/auto`, `sin propiedad`) | Registro patrimonial | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Activos preexistentes del cliente. |
| **`age`** | Edad del solicitante | Numérica discreta (Años cumplidos) | Documento de identidad | Al momento de la solicitud | Imputación mediana + StandardScaler | **Riesgo ético/sesgo:** Variable demográfica protegida; sin riesgo de fuga temporal. |
| **`other_payment_plans`** | Otros planes de financiamiento o cuotas en curso | Categórica (`banco`, `almacén`, `ninguno`) | Buró crediticio | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Carga financiera preexistente. |
| **`housing`** | Tipo de vivienda | Categórica (`propia`, `alquilada`, `gratuita`) | Declaración / Comprobante | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Situación habitacional al momento de solicitar. |
| **`existing_credits`** | Número de créditos vigentes en este banco | Numérica discreta (Conteo entero) | Sistema central bancario | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Exposición crediticia previa en la entidad. |
| **`job`** | Calificación o nivel del empleo | Categórica (`desempleado/no calificado`, `calificado`, `autónomo/gerencial`) | Declaración de ingresos / RNC | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Perfil ocupacional formal previo. |
| **`num_dependents`** | Personas dependientes a cargo | Numérica discreta (Conteo: 1 o 2+) | Declaración del solicitante | Al momento de la solicitud | Imputación mediana + StandardScaler | **Bajo.** Carga familiar conocida antes del crédito. |
| **`own_telephone`** | Posee teléfono registrado a su nombre | Categórica binaria (`sí`, `no`) | Formulario de contacto | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Bajo.** Dato de contacto inicial. |
| **`foreign_worker`** | Es trabajador extranjero | Categórica binaria (`sí`, `no`) | Estatus migratorio / Permiso laboral | Al momento de la solicitud | Imputación moda + OneHotEncoder | **Riesgo ético/sesgo:** Condición sensible sujeta a escrutinio para evitar sesgo crediticio; sin fuga. |
| **`class` (TARGET)** | Comportamiento final del crédito (Riesgo) | Binario (1 = Buen riesgo / pagador; 2 = Mal riesgo / incumplidor) | Registro contable histórico tras el periodo del crédito | **Ex-post (Desenlace posterior)** | Aislamiento en vector $y$ (no entra a transformaciones de $X$) | **Fuga crítica si se deja en $X$.** Debe extraerse estrictamente como objetivo para no contaminar las características. |


# Diccionario de Datos Oficial y Auditoría Semántica (U01.LAB02)
**Dataset:** Statlog (German Credit Data) — UCI ID: 144  
**Unidad de análisis:** Solicitante individual de crédito  
**Decisión:** Aprobación o denegación de la solicitud de crédito mitigando el riesgo de impago  

---

### Tabla Detallada de Atributos

| Columna / Variable | Atributo UCI | Significado Semántico | Categorías y Valores Oficiales (Codificación UCI) | Momento de Disponibilidad | Transformación en Pipeline | Análisis de Riesgo (Fuga / Sesgo) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`checking_status`** | Attribute 1 | Estado de la cuenta corriente existente | • **A11:** < 0 DM<br>• **A12:** 0 <= ... < 200 DM<br>• **A13:** >= 200 DM / nómina asignada por al menos 1 año<br>• **A14:** Sin cuenta corriente | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Información financiera preexistente en la entidad o buró. |
| **`duration`** | Attribute 2 | Plazo del crédito solicitado | Numérico continuo/discreto (Duración en meses) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Condición contractual establecida ex-ante. |
| **`credit_history`** | Attribute 3 | Historial crediticio previo | • **A30:** No ha tomado créditos / todos pagados debidamente<br>• **A31:** Créditos en este banco pagados debidamente<br>• **A32:** Créditos existentes pagados debidamente hasta la fecha<br>• **A33:** Retrasos en pagos en el pasado<br>• **A34:** Cuenta crítica / otros créditos existentes (en otros bancos) | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Historial estrictamente retrospectivo antes de la solicitud actual. |
| **`purpose`** | Attribute 4 | Propósito / Destino del crédito | • **A40:** Automóvil (nuevo)<br>• **A41:** Automóvil (usado)<br>• **A42:** Muebles / equipamiento<br>• **A43:** Radio / televisión<br>• **A44:** Electrodomésticos<br>• **A45:** Reparaciones<br>• **A46:** Educación<br>• **A47:** Vacaciones<br>• **A48:** Capacitación / reconversión laboral<br>• **A49:** Negocios<br>• **A410:** Otros | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Declarado por el solicitante en la solicitud. |
| **`credit_amount`** | Attribute 5 | Monto del crédito solicitado | Numérico continuo (Monto en Marcos Alemanes - DM) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Magnitud del capital solicitado antes de la aprobación. |
| **`savings_status`** | Attribute 6 | Cuentas de ahorros y bonos | • **A61:** < 100 DM<br>• **A62:** 100 <= ... < 500 DM<br>• **A63:** 500 <= ... < 1000 DM<br>• **A64:** >= 1000 DM<br>• **A65:** Desconocido / no tiene cuenta de ahorros | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Ahorro patrimonial acumulado previo. |
| **`employment`** | Attribute 7 | Tiempo en el empleo actual | • **A71:** Desempleado<br>• **A72:** < 1 año<br>• **A73:** 1 <= ... < 4 años<br>• **A74:** 4 <= ... < 7 años<br>• **A75:** >= 7 años | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Estabilidad laboral verificable ex-ante. |
| **`installment_commitment`** | Attribute 8 | Tasa de pago en porcentaje del ingreso | Numérico discreto (1, 2, 3, 4 correspondiente al % de la cuota respecto al ingreso disponible) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Capacidad de pago estimada al momento de solicitud. |
| **`personal_status`** | Attribute 9 | Estado personal, estado civil y sexo | • **A91:** Masculino: divorciado/separado<br>• **A92:** Femenino: divorciada/separada/casada<br>• **A93:** Masculino: soltero<br>• **A94:** Masculino: casado/viudo<br>• **A95:** Femenino: soltera | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Riesgo de sesgo/ética.** Atributo demográfico sensible. No genera fuga temporal, pero exige monitoreo de equidad (*fairness*). |
| **`other_parties`** | Attribute 10 | Otros deudores o garantes | • **A101:** Ninguno<br>• **A102:** Co-solicitante<br>• **A103:** Garante | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Estructura de garantías preexistente. |
| **`residence_since`** | Attribute 11 | Tiempo de residencia en el domicilio actual | Numérico discreto (Años: 1, 2, 3, 4) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Estabilidad domiciliaria histórica. |
| **`property_magnitude`** | Attribute 12 | Propiedades o bienes de mayor valor | • **A121:** Bienes raíces (inmueble)<br>• **A122:** Sociedad de ahorro hipotecario / seguro de vida<br>• **A123:** Automóvil u otro (no incluido en ahorros)<br>• **A124:** Desconocido / sin propiedad | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Declaración patrimonial inicial. |
| **`age`** | Attribute 13 | Edad del solicitante | Numérico discreto (Años cumplidos) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Riesgo de sesgo.** Variable protegida; sin fuga temporal. |
| **`other_payment_plans`** | Attribute 14 | Otros planes de financiamiento a plazos | • **A141:** Banco<br>• **A142:** Tiendas / almacenes comerciales<br>• **A143:** Ninguno | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Compromisos de pago contraídos con terceros antes del crédito. |
| **`housing`** | Attribute 15 | Tipo de vivienda | • **A151:** Alquilada<br>• **A152:** Propia<br>• **A153:** Gratuita (cedida / sin costo) | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Situación habitacional al momento de solicitar. |
| **`existing_credits`** | Attribute 16 | Número de créditos vigentes en este banco | Numérico discreto (Conteo entero: 1, 2, 3, 4) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Registro contable interno previo del cliente. |
| **`job`** | Attribute 17 | Nivel de calificación laboral | • **A171:** Desempleado / no calificado - no residente<br>• **A172:** No calificado - residente<br>• **A173:** Empleado calificado / funcionario<br>• **A174:** Dirección / autónomo / altamente calificado / oficial | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Perfil profesional evaluado antes de dictaminar. |
| **`num_dependents`** | Attribute 18 | Número de personas a cargo | Numérico discreto (Conteo: 1 o 2+) | Al momento de la solicitud | `SimpleImputer(strategy='median')` + `StandardScaler()` | **Sin fuga.** Obligaciones familiares conocidas ex-ante. |
| **`own_telephone`** | Attribute 19 | Teléfono a nombre del cliente | • **A191:** Ninguno<br>• **A192:** Sí, registrado a nombre del cliente | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Sin fuga.** Canal de localización al momento de contacto. |
| **`foreign_worker`** | Attribute 20 | Condición de trabajador extranjero | • **A201:** Sí<br>• **A202:** No | Al momento de la solicitud | `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` | **Riesgo ético/sesgo.** Variable sensible migratoria. No genera fuga de datos, pero requiere cautela analítica. |
| **`class` (TARGET)** | Atributo 21 (Objetivo) | Riesgo de crédito final | • **1:** Buen pagador / Bajo riesgo (*Good*)<br>• **2:** Incumplidor / Mal crédito (*Bad*) | **Posterior (Ex-post)** | Se separa en vector `y` y se excluye de `X` | **Fuga crítica si se mantiene en X.** Solo se conoce tras transcurrir el período del préstamo. |