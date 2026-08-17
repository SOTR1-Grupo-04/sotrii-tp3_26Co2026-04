# TP3 – Actividad 02 – Rate Monotonic

## Notación

| Símbolo | Significado                       |
|:--------|:----------------------------------|
| C       | Tiempo máximo de ejecución (WCET) |
| P       | Período de activación             |
| D       | Plazo de finalización (deadline)  |
| U       | Factor de carga CPU               |
| H       | Hiperperíodo: mcm de los P_i      |
| R       | Tiempo de respuesta               |

En todos los sistemas del enunciado se cumple **P = D**.

### Test de garantía (Rate Monotonic)

Para tareas periódicas con **P = D**, Rate Monotonic asigna prioridades fijas según el período: a menor período, mayor prioridad. Siguiendo el criterio de FreeRTOS, un valor numérico de prioridad más alto representa una prioridad mayor.

| Test | Condición | Significado |
|:----:|:----------|:------------|
| Suficiencia | U <= n(2^(1/n) - 1) | Si cumple, el sistema es planificable. Si no, el test es no concluyente. |
| Exacto (RTA) | R_i <= D_i | Verifica el tiempo de respuesta de cada tarea. |

Para el análisis exacto se itera:

```
w_i^(k+1) = C_i + SUM(ceil(w_i^k / P_j) * C_j), para toda tarea j de mayor prioridad
```

**Criterio de planificabilidad:** el sistema es **planificable** si el test de suficiencia lo garantiza o si todas las tareas cumplen **R_i <= D_i** mediante RTA.

### Carga de CPU

Carga de cada tarea = **WCET / Período** = **C / P**.

Carga del sistema:

```
U = SUM(C_i / P_i) <= 1   (<= 100%)
```

Si U > 100%, el sistema no es planificable.

---

## Sistema 1

| Tarea | C | P = D | Prioridad |
|:------|:-:|:-----:|:---------:|
| T1    | 1 |   4   | 3 (mayor) |
| T2    | 2 |   5   |     2     |
| T3    | 5 |  20   | 1 (menor) |

### Carga de CPU

| Tarea | Período (P) | WCET (C) | Carga CPU |
|:-----:|:-----------:|:--------:|:---------:|
| T1 | 4 | 1 | 1/4 = **25%** |
| T2 | 5 | 2 | 2/5 = **40%** |
| T3 | 20 | 5 | 5/20 = **25%** |
| **Total** | | | **U = 90%** |

### Hiperperíodo

```
H = mcm(4, 5, 20) = 20
```

### Test de garantía

Para n = 3, el límite de Liu y Layland es aproximadamente **77,9%**.

| Test | Resultado |
|:-----|:----------|
| Suficiencia | 90% > 77,9% → no concluyente |
| RTA — T1 | R_1 = 1 <= 4 → cumple |
| RTA — T2 | R_2 = 3 <= 5 → cumple |
| RTA — T3 | R_3 = 15 <= 20 → cumple |
| **Planificable** | **Sí** (RTA cumple para todas las tareas) |

#### Cálculo RTA de T2

```
w_2^0 = 2
w_2^1 = 2 + ceil(2 / 4) * 1 = 3
w_2^2 = 3
R_2 = 3 <= 5
```

#### Cálculo RTA de T3

```
w_3^0 = 5
w_3^1 = 5 + ceil(5 / 4) * 1 + ceil(5 / 5) * 2 = 9
w_3^2 = 12
w_3^3 = 14
w_3^4 = 15
w_3^5 = 15
R_3 = 15 <= 20
```

### Diagrama de Gantt (resumen)

| Instante | Ejecución |
|:--------:|:----------|
| 0 | T1(1), luego T2(2) y T3(1) |
| 4 | T1 se activa, desaloja a T3, ejecuta 1 u.t.; T3 continúa 4 u.t. |
| 5 | T2 se activa y ejecuta 2 u.t. |

---

## Sistema 2

| Tarea | C | P = D | Prioridad |
|:------|:-:|:-----:|:---------:|
| T1 | 1 | 6 | 3 (mayor) |
| T2 | 2 | 10 | 2 |
| T3 | 2 | 18 | 1 (menor) |

### Carga de CPU

| Tarea | Período (P) | WCET (C) | Carga CPU |
|:-----:|:-----------:|:--------:|:---------:|
| T1 | 6 | 1 | 1/6 = **16,7%** |
| T2 | 10 | 2 | 2/10 = **20%** |
| T3 | 18 | 2 | 2/18 = **11,1%** |
| **Total** | | | **U = 47,7%** |

### Hiperperíodo

```
H = mcm(6, 10, 18) = 90
```

### Test de garantía

Para n = 3, el límite de Liu y Layland es aproximadamente **77,9%**.

| Test | Resultado |
|:-----|:----------|
| Suficiencia | 47,7% <= 77,9% → cumple |
| **Planificable** | **Sí** (garantizado por el test de suficiencia) |

---

## Sistema 3

| Tarea | C | P = D | Prioridad |
|:------|:-:|:-----:|:---------:|
| T1 | 1 | 8 | 4 (mayor) |
| T2 | 3 | 15 | 3 |
| T3 | 4 | 20 | 2 |
| T4 | 6 | 22 | 1 (menor) |

### Carga de CPU

| Tarea | Período (P) | WCET (C) | Carga CPU |
|:-----:|:-----------:|:--------:|:---------:|
| T1 | 8 | 1 | 1/8 = **12,5%** |
| T2 | 15 | 3 | 3/15 = **20%** |
| T3 | 20 | 4 | 4/20 = **20%** |
| T4 | 22 | 6 | 6/22 = **27,3%** |
| **Total** | | | **U = 79,7%** |

### Hiperperíodo

```
H = mcm(8, 15, 20, 22) = 1320
```

### Test de garantía

Para n = 4, el límite de Liu y Layland es aproximadamente **75,6%**.

| Test | Resultado |
|:-----|:----------|
| Suficiencia | 79,7% > 75,6% → no concluyente |
| RTA — T1 | R_1 = 1 <= 8 → cumple |
| RTA — T2 | R_2 = 4 <= 15 → cumple |
| RTA — T3 | R_3 = 8 <= 20 → cumple |
| RTA — T4 | R_4 = 15 <= 22 → cumple |
| **Planificable** | **Sí** (RTA cumple para todas las tareas) |

#### Cálculo RTA de T1

```
R_1 = C_1 = 1 <= 8
```

#### Cálculo RTA de T2

```
w_2^0 = 3
w_2^1 = 3 + ceil(3 / 8) * 1 = 4
w_2^2 = 3 + ceil(4 / 8) * 1 = 4
R_2 = 4 <= 15
```

#### Cálculo RTA de T3

```
w_3^0 = 4
w_3^1 = 4 + ceil(4 / 8) * 1 + ceil(4 / 15) * 3 = 8
w_3^2 = 4 + ceil(8 / 8) * 1 + ceil(8 / 15) * 3 = 8
R_3 = 8 <= 20
```

#### Cálculo RTA de T4

```
w_4^0 = 6
w_4^1 = 6 + ceil(6 / 8) * 1 + ceil(6 / 15) * 3 + ceil(6 / 20) * 4 = 14
w_4^2 = 6 + ceil(14 / 8) * 1 + ceil(14 / 15) * 3 + ceil(14 / 20) * 4 = 15
w_4^3 = 6 + ceil(15 / 8) * 1 + ceil(15 / 15) * 3 + ceil(15 / 20) * 4 = 15
R_4 = 15 <= 22
```

---

## Sistema 4

| Tarea | C | P = D | Prioridad |
|:------|:-:|:-----:|:---------:|
| T1 | 0,5 | 4 | 4 (mayor) |
| T2 | 1 | 5 | 3 |
| T3 | 2 | 10 | 2 |
| T4 | 9 | 24 | 1 (menor) |

### Carga de CPU

| Tarea | Período (P) | WCET (C) | Carga CPU |
|:-----:|:-----------:|:--------:|:---------:|
| T1 | 4 | 0,5 | 0,5/4 = **12,5%** |
| T2 | 5 | 1 | 1/5 = **20%** |
| T3 | 10 | 2 | 2/10 = **20%** |
| T4 | 24 | 9 | 9/24 = **37,5%** |
| **Total** | | | **U = 90%** |

### Hiperperíodo

```
H = mcm(4, 5, 10, 24) = 120
```

### Test de garantía

Para n = 4, el límite de Liu y Layland es aproximadamente **75,6%**.

| Test | Resultado |
|:-----|:----------|
| Suficiencia | 90% > 75,6% → no concluyente |
| RTA — T1 | R_1 = 0,5 <= 4 → cumple |
| RTA — T2 | R_2 = 1,5 <= 5 → cumple |
| RTA — T3 | R_3 = 3,5 <= 10 → cumple |
| RTA — T4 | R_4 = 19,5 <= 24 → cumple |
| **Planificable** | **Sí** (RTA cumple para todas las tareas) |

#### Cálculo RTA de T1

```
R_1 = C_1 = 0,5 <= 4
```

#### Cálculo RTA de T2

```
w_2^0 = 1
w_2^1 = 1 + ceil(1 / 4) * 0,5 = 1,5
w_2^2 = 1 + ceil(1,5 / 4) * 0,5 = 1,5
R_2 = 1,5 <= 5
```

#### Cálculo RTA de T3

```
w_3^0 = 2
w_3^1 = 2 + ceil(2 / 4) * 0,5 + ceil(2 / 5) * 1 = 3,5
w_3^2 = 2 + ceil(3,5 / 4) * 0,5 + ceil(3,5 / 5) * 1 = 3,5
R_3 = 3,5 <= 10
```

#### Cálculo RTA de T4

```
w_4^0 = 9
w_4^1 = 9 + 3(0,5) + 2(1) + 1(2) = 14,5
w_4^2 = 9 + 4(0,5) + 3(1) + 2(2) = 18
w_4^3 = 9 + 5(0,5) + 4(1) + 2(2) = 19,5
w_4^4 = 9 + 5(0,5) + 4(1) + 2(2) = 19,5
R_4 = 19,5 <= 24
```

## Configuración FreeRTOS (Paso 03)

Para implementar un **sistema Rate Monotonic (RM) en FreeRTOS** de forma eficiente y determinista, se propone la siguiente configuración basada en los requerimientos técnicos de las fuentes:
* Verificación de Carga: Asegurar que el factor de utilización total (U) sea menor a 1 (100%) y si es necesario hacer el Análisis de Tiempo de Respuesta (RTA) para garantizar que cada tarea finalice antes de su próximo periodo para saber la validez del sistema propuesto.
* Planificador Expulsivo: Configurar configUSE_PREEMPTION en 1 en FreeRTOSConfig.h para que las tareas de mayor prioridad puedan desalojar a las de menor prioridad inmediatamente al activarse
* Asignación de Prioridades Estáticas: Asignar niveles de prioridad de forma inversa al periodo de cada tarea; la tarea con el periodo más corto recibe la prioridad numérica más alta en FreeRTOS
* Mecanismo de Activación Periódica: Cada tarea debe tener un timer y un semaforo asociados para que sea el que al hacer timeout el timer, haga un give del semaforo y la tarea corra en  cada periodo. 
* Independencia de Tareas: Evitar el uso de recursos compartidos o secciones críticas que puedan causar inversión de prioridades, manteniendo las tareas como entidades independientes
* Monitoreo de Tiempos (Safety): Implementar un Monitor de Tareas para verificar que ninguna tarea exceda su WCET (peor tiempo de ejecución) y un Watchdog Timer para resetear el sistema en caso de fallos de tiempo