# TP3 – Actividad 02 – Rate Monolitic

## Notación

| Símbolo | Significado                                      |
|:--------|:-------------------------------------------------|
| C       | Tiempo máximo de ejecución (WCET)                |
| P       | Período de activación (= T del enunciado)        |
| D       | Plazo de finalización (deadline)                 |
| U       | Factor de carga CPU                              |
| T_M     | Hiperperíodo (ciclo mayor): mcm de todos los P_i |
| T_s     | Ciclo secundario (tamaño de trama)               |
| F       | Cantidad de tramas por hiperperíodo: T_M / T_s   |

En todos los sistemas del enunciado se cumple **P = D**.

### Test de garantía (planificación estática/cíclica)

Para garantizar el cumplimiento de una planificación estática/cíclica (periódica):

1) Sis se cumple  
2)
**Criterio de planificabilidad:** el sistema es **planificable** si y solo si se cumplen **las cinco ecuaciones**.

### Prioridades

Se asignan de forma estática. Criterio: **deadline monotonic** (menor período (T) implica mayor prioridad).

### Carga de CPU

Carga de cada tarea = **WCET / Period** = **C / T**.

Carga del sistema:

```
U = SUM(Ci / Ti) <= 1   (<= 100%)
```

Si U > 100%, el sistema no es planificable (incumple ecuación **(2)**).

---
# Sistema 1

**Tareas:** T1(1, 4, 4), T2(2, 5, 5), T3(5, 20, 20).

## 1. Asignación de prioridades

- **P1 (Alta):** T1 ($T = 4$)
- **P2 (Media):** T2 ($T = 5$)
- **P3 (Baja):** T3 ($T = 20$)

## 2. Cálculos base

- **Factor de Uso (U):**

  $$
  U = \frac{1}{4} + \frac{2}{5} + \frac{5}{20}
  = 0,25 + 0,4 + 0,25
  = \mathbf{0,90}
  $$

- **Hiperperíodo (H):**

  $$
  H = \operatorname{mcm}(4,5,20) = \mathbf{20}
  $$

- **Período Secundario ($T_S$):**

  $$
  T_S = \operatorname{mcd}(4,5,20) = \mathbf{1}
  $$

## 3. Test de garantía

- **Suficiencia:** Para $N = 3$, el límite es aproximadamente $0,779$.

  $$
  0,90 > 0,779
  $$

  Por lo tanto, el test no es concluyente.

- **Exacto (RTA):**

  - $R_1 = 1 \leq 4$ → **OK**

  - Para $T_2$:

    $$
    w_2^0 = 2
    $$

    $$
    w_2^1 = 2 + \left\lceil \frac{2}{4} \right\rceil 1 = 3
    $$

    $$
    w_2^2 = 3
    $$

    Por lo tanto:

    $$
    R_2 = 3 \leq 5
    $$

    → **OK**

  - Para $T_3$:

    $$
    w_3^0 = 5
    $$

    $$
    w_3^1 =
    5 +
    \left\lceil \frac{5}{4} \right\rceil 1 +
    \left\lceil \frac{5}{5} \right\rceil 2
    = 9
    $$

    $$
    w_3^2 = 12
    $$

    $$
    w_3^3 = 14
    $$

    $$
    w_3^4 = 15
    $$

    $$
    w_3^5 = 15
    $$

    Por lo tanto:

    $$
    R_3 = 15 \leq 20
    $$

    → **OK**

- **Resultado:** El sistema es **planificable**.

## 4. Diagrama de Gantt (resumen)

- $t = 0$: Ejecuta T1(1). Luego T2(2). Luego T3(1).
- $t = 4$: T1 se activa y desaloja a T3. Ejecuta T1(1). Luego continúa T3(4).
- $t = 5$: T2 se activa. Ejecuta T2(2).

---

# Sistema 2

**Tareas:** T1(1, 6, 6), T2(2, 10, 10), T3(2, 18, 18).

## 1. Asignación de prioridades

- **P1:** T1 ($T = 6$)
- **P2:** T2 ($T = 10$)
- **P3:** T3 ($T = 18$)

## 2. Cálculos base

- **Factor de Uso (U):**

  $$
  U =
  \frac{1}{6} +
  \frac{2}{10} +
  \frac{2}{18}
  \approx
  0,166 + 0,2 + 0,111
  = \mathbf{0,477}
  $$

- **Hiperperíodo (H):**

  $$
  H = \operatorname{mcm}(6,10,18) = \mathbf{90}
  $$

- **Período Secundario ($T_S$):**

  $$
  T_S = \operatorname{mcd}(6,10,18) = \mathbf{2}
  $$

## 3. Test de garantía

- **Suficiencia:**

  $$
  0,477 \leq 0,779
  $$

- **Resultado:** El sistema es **planificable**, garantizado por el test de suficiencia.

---

# Sistema 3

**Tareas:** T1(1, 8, 8), T2(3, 15, 15), T3(4, 20, 20), T4(6, 22, 22).

## 1. Asignación de prioridades

- **P1:** T1
- **P2:** T2
- **P3:** T3
- **P4:** T4

## 2. Cálculos base

- **Factor de Uso (U):**

  $$
  U =
  \frac{1}{8} +
  \frac{3}{15} +
  \frac{4}{20} +
  \frac{6}{22}
  \approx
  0,125 + 0,2 + 0,2 + 0,272
  = \mathbf{0,797}
  $$

- **Hiperperíodo (H):**

  $$
  H = \operatorname{mcm}(8,15,20,22) = \mathbf{1320}
  $$

- **Período Secundario ($T_S$):**

  $$
  T_S = \operatorname{mcd}(8,15,20,22) = \mathbf{1}
  $$

## 3. Test de garantía

- **Suficiencia:** Para $N = 4$, el límite es aproximadamente $0,756$.

  $$
  0,797 > 0,756
  $$

  Por lo tanto, el test no es concluyente.

- **Exacto (RTA):**

  - $R_1 = 1$
  - $R_2 = 4$
  - $R_3 = 8$

  Todos cumplen sus respectivos deadlines.

  Para $T_4$:

  $$
  w_4^0 = 6
  $$

  $$
  w_4^1 =
  6 +
  \left\lceil \frac{6}{8} \right\rceil 1 +
  \left\lceil \frac{6}{15} \right\rceil 3 +
  \left\lceil \frac{6}{20} \right\rceil 4
  = 14
  $$

  $$
  w_4^2 = 15
  $$

  $$
  w_4^3 = 15
  $$

  Por lo tanto:

  $$
  R_4 = 15 \leq 22
  $$

  → **OK**

- **Resultado:** El sistema es **planificable**.

---

# Sistema 4

**Tareas:** T1(0,5, 4, 4), T2(1, 5, 5), T3(2, 10, 10), T4(9, 24, 24).

## 1. Asignación de prioridades

- **P1:** T1
- **P2:** T2
- **P3:** T3
- **P4:** T4

## 2. Cálculos base

- **Factor de Uso (U):**

  $$
  U =
  \frac{0,5}{4} +
  \frac{1}{5} +
  \frac{2}{10} +
  \frac{9}{24}
  = 0,125 + 0,2 + 0,2 + 0,375
  = \mathbf{0,90}
  $$

- **Hiperperíodo (H):**

  $$
  H = \operatorname{mcm}(4,5,10,24) = \mathbf{120}
  $$

- **Período Secundario ($T_S$):**

  $$
  T_S = \operatorname{mcd}(4,5,10,24) = \mathbf{1}
  $$

## 3. Test de garantía

- **Suficiencia:**

  $$
  0,90 > 0,756
  $$

  Por lo tanto, el test no es concluyente.

- **Exacto (RTA):**

  - $R_1 = 0,5$
  - $R_2 = 1,5$
  - $R_3 = 3,5$

  Todos cumplen sus respectivos deadlines.

  Para $T_4$:

  $$
  w_4^0 = 9
  $$

  $$
  w_4^1 = 9 + 3(0,5) + 2(1) + 1(2) = 14,5
  $$

  $$
  w_4^2 = 18
  $$

  $$
  w_4^3 = 19,5
  $$

  $$
  w_4^4 = 19,5
  $$

  Por lo tanto:

  $$
  R_4 = 19,5 \leq 24
  $$

  → **OK**

- **Resultado:** El sistema es **planificable**.