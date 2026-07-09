---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
---

# 紊流動能方程式 (Turbulent Kinetic Energy Equation, TKE)

從 **【已知 1】動量方程式 (Momentum Equation)** 出發，經兩步得到紊流動能方程式：

1. **Step 1**：雷諾分解後，工作方程式減去平均動量方程式，得 **擾動動量方程式 (Perturbation Momentum Equation)**。
2. **Step 2**：整條方程式乘上 $u'_i$ 並取系集平均，逐項化簡後直接整理成標準 TKE 方程式。

本推導的**核心亮點**：科氏力項 $-2\varepsilon_{ijk}\Omega_j u'_k$ 中，$\varepsilon_{ijk}$ **全反對稱**而 $u'_i u'_k$ **對稱**，雙重縮併必為零（【推導 4】）。這一眼就看出「科氏力不做功」，完全免去傳統向量微積分中 $\mathbf{u}'\cdot(\boldsymbol{\Omega}\times\mathbf{u}')=0$ 的外積展開。

> **符號釐清**：本檔的 $\varepsilon$ 有兩種用法，靠**指標數量**區分，不會混淆——
> $\varepsilon_{ijk}$（**三個指標**）是 Levi-Civita 符號；$\varepsilon$（**無指標**）是黏滯耗散率（【定義 2】）。

+++

## 假設與已知 (Assumptions & Preliminaries)

> 先把所有武器編號攤開，之後的 `## 證明` 只做「引用」。

* **【已知 1】 [動量方程式 (Momentum Equation, Navier–Stokes)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#momentum-equation-navier-stokes)** ： 以愛因斯坦求和約定改寫，並令 $\mathbf{g}$ 指向 $-z$，即 $g_i = -g\,\delta_{i3}$。

  $$\begin{gather*}
  \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} &=& \mathbf{g} - \frac{1}{\rho} \nabla P + \frac{\mu}{\rho} \nabla^2 \mathbf{u} \\
  \frac{\partial u_i}{\partial t} + u_j \frac{\partial u_i}{\partial x_j} &=& -g\,\delta_{i3} - \frac{1}{\rho}\frac{\partial P}{\partial x_i} + \frac{\mu}{\rho}\frac{\partial^2 u_i}{\partial x_j \partial x_j}
  \end{gather*}$$

  * $\mathbf{u}$ : $3$ 維速度向量 (velocity vector) $[\text{m}\cdot\text{s}^{-1}]$
  * $P$ : 壓力 (pressure) $[\text{Pa}]$
  * $\rho$ : 密度 (density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $\mu$ : 動力黏滯係數 (dynamic viscosity) $[\text{Pa}\cdot\text{s}]$
  * $\mathbf{g}$ : 重力加速度向量 (gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$

  * $u_i$ : 速度分量 (velocity component) $[\text{m}\cdot\text{s}^{-1}]$
  * $x_i$ : 座標分量 (coordinate) $[\text{m}]$
  * $t$ : 時間 (time) $[\text{s}]$
  * $g$ : 重力加速度大小 (gravity) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81\ \text{m}\cdot\text{s}^{-2}$

* **【已知 2】 張量工具 (Tensor Toolbox)** ：詳見 [Levi-Civita symbol 主筆記](./Levi-Civita_symbol.ipynb)。

  * **(a-1) Levi-Civita 符號的全反對稱性 (total antisymmetry)**：交換任兩個指標即變號。

    $$\varepsilon_{ijk} = -\varepsilon_{kji}$$

  * **(a-2) 以 Levi-Civita 符號展開外積 (cross product)**：本檔以 $\overset{\text{LC}}{=}$ 標記這一步。

    $$(\mathbf{a} \times \mathbf{b})_i \overset{\text{LC}}{=} \varepsilon_{ijk}\, a_j\, b_k$$

    * $\varepsilon_{ijk}$ : Levi-Civita 符號分量 (Levi-Civita symbol)，值為 $\pm 1$ 或 $0$
    * $\mathbf{a},\ \mathbf{b}$ : $3$ 維向量 (3-dim vector)
    * $i,j,k$ : 指標 (index)，取值 $1,2,3$；重複指標依愛因斯坦求和約定 ($\overset{\text{Esc}}{=}$) 對 $1$ 到 $3$ 求和

  * **(b-1) Kronecker delta 的定義 (definition)**

    $$\delta_{ij} \overset{\text{def}}{=} \begin{cases} 1 & (i=j) \\ 0 & (i \ne j)\end{cases}$$

    * $\delta_{ij}$ : Kronecker delta 分量 (Kronecker delta)，值為 $1$ 或 $0$

  * **(b-2) Kronecker delta 的篩選性質 (sifting property)**：與 $\delta$ 縮併，等於把啞指標換成 $\delta$ 的另一個指標。

    $$\delta_{i3}\, A_i = A_3$$

    * $A_i$ : 任意帶指標量 (any indexed quantity)

* **【已知 3】 雷諾平均律 (Reynolds Averaging Rules)** ：系集平均 $\overline{(\cdot)}$ 的五條運算規則。設 $a,\ b$ 為任意場量，$a'$ 為擾動量、$\bar{a}$ 為平均量。

  * **(a) 線性 (linearity)**

    $$\overline{a + b} = \bar{a} + \bar{b}$$

  * **(b) 擾動的平均為零 (zero mean of perturbation)**

    $$\overline{a'} = 0$$

  * **(c) 平均量可提出平均之外 (mean is deterministic)**

    $$\overline{\bar{a}} = \bar{a}, \qquad \overline{\bar{a}\, b} = \bar{a}\,\bar{b}$$

  * **(d) 與空間微分可交換 (commutes with spatial derivative)**

    $$\overline{\frac{\partial a}{\partial x_j}} = \frac{\partial \bar{a}}{\partial x_j}$$

  * **(e) 與時間微分可交換 (commutes with time derivative)**

    $$\overline{\frac{\partial a}{\partial t}} = \frac{\partial \bar{a}}{\partial t}$$

* **【假設 1】 雷諾分解 (Reynolds Decomposition)** ：任一場量拆成「系集平均 + 擾動」。本檔採**系集平均**（對大量實現取平均），故平均量與擾動量**都是 $(x,y,z,t)$ 的函數**（例如 $u_i(x,y,z,t) = \bar{u}_i(x,y,z,t) + u'_i(x,y,z,t)$）；因為自變數完全相同，以下一律省略不寫。唯一的例外是【假設 3(c)】的基本態壓力 $P_0(z)$，它**只**依賴高度，那裡才特別標出自變數。

  * **(a) 速度 (velocity)**

    $$u_i = \bar{u}_i + u'_i$$

    * $\bar{u}_i$ : 平均速度 (mean velocity) $[\text{m}\cdot\text{s}^{-1}]$
    * $u'_i$ : 擾動速度 (velocity perturbation) $[\text{m}\cdot\text{s}^{-1}]$；並令 $w' \overset{\text{let}}{=} u'_3$ 為垂直擾動速度

  * **(b) 壓力 (pressure)**

    $$p = \bar{p} + p'$$

    * $\bar{p}$ : 平均擾動壓力 (mean of $p$) $[\text{Pa}]$
    * $p'$ : 壓力擾動 (pressure perturbation) $[\text{Pa}]$

  * **(c) 密度 (density)**：這裡被分解的是密度**偏差** $\tilde{\rho}$（其定義見【假設 3(a)】），不是總密度 $\rho$。

    $$\tilde{\rho} = \bar{\rho} + \rho'$$

    * $\bar{\rho}$ : 密度偏差的平均 (mean of $\tilde{\rho}$) $[\text{kg}\cdot\text{m}^{-3}]$
    * $\rho'$ : 密度擾動 (density perturbation) $[\text{kg}\cdot\text{m}^{-3}]$

* **【假設 2】 不可壓縮 (Incompressibility)** ：連續方程式退化為速度場無散度。

  * **(a) 全速度場無散度 (divergence-free)**

    $$\frac{\partial u_i}{\partial x_i} = 0$$

  * **(b) 平均場無散度**

    $$\begin{gather*}
    \frac{\partial \bar{u}_i}{\partial x_i} &\overset{\text{已知 3(d)}}{=}& \overline{\frac{\partial u_i}{\partial x_i}} \\
    &\overset{\text{假設 2(a)}}{=}& \overline{0} \\
    &=& 0
    \end{gather*}$$

  * **(c) 擾動場無散度**

    $$\begin{gather*}
    0 &\overset{\text{假設 2(a)}}{=}& \frac{\partial u_i}{\partial x_i} \\
    &\overset{\text{假設 1(a)}}{=}& \frac{\partial \bar{u}_i}{\partial x_i} + \frac{\partial u'_i}{\partial x_i} \\
    &\overset{\text{假設 2(b)}}{=}& \frac{\partial u'_i}{\partial x_i}
    \end{gather*}$$

* **【假設 3】 Boussinesq 近似 (Boussinesq Approximation)** ：把密度寫成「常數參考值 $\rho_0$ ＋微小偏差 $\tilde{\rho}$」，並約定 $\tilde{\rho}$ **只在重力（浮力）項中保留**，其餘各項一律以 $\rho_0$ 取代 $\rho$。以下 (a)(b)(c) 分別處理密度、黏滯係數、壓力三個場量。

  * **(a) 密度分解 (density decomposition)**：$\tilde{\rho}$ 是 $\rho$ 對參考值 $\rho_0$ 的偏差，且假設它遠小於 $\rho_0$；故在浮力項以外的地方 $\rho$ 可直接近似為常數 $\rho_0$。

    $$\begin{gather*}
    \rho(x,y,z,t) &\overset{\text{let}}{=}& \rho_0 + \tilde{\rho}(x,y,z,t)\ , \qquad |\tilde{\rho}| \ll \rho_0 \\
    &\approx& \rho_0
    \end{gather*}$$

    * $\rho_0$ : 常數參考密度 (constant reference density) $[\text{kg}\cdot\text{m}^{-3}]$，純量常數
    * $\tilde{\rho}$ : 密度對 $\rho_0$ 的偏差 (density deviation) $[\text{kg}\cdot\text{m}^{-3}]$，純量場；其雷諾分解見【假設 1(c)】

  * **(b) 運動黏滯係數為常數 (constant kinematic viscosity)**：由 (a) 的 $\rho \approx \rho_0$，$\nu$ 可提到微分之外。

    $$\begin{gather*}
    \nu &\overset{\text{def}}{=}& \frac{\mu}{\rho} \\
    &\overset{\text{假設 3(a)}}{\approx}& \frac{\mu}{\rho_0} \ =\ \text{常數}
    \end{gather*}$$

    * $\nu$ : 運動黏滯係數 (kinematic viscosity) $[\text{m}^2\cdot\text{s}^{-1}]$，純量常數
    * $\mu$ : 動力黏滯係數 (dynamic viscosity) $[\text{Pa}\cdot\text{s}]$，見【已知 1】

  * **(c) 壓力分解 (pressure decomposition)**：【已知 1】裡的 $P$ 是**總壓力**。把它拆成「只隨高度變化的基本態 $P_0(z)$」與「其餘部分 $p$」；並要求 $P_0$ 與參考密度 $\rho_0$ 滿足**靜力平衡 (hydrostatic balance)**，$\dfrac{\mathrm{d}P_0}{\mathrm{d}z} = -\rho_0\, g$。第二列成立是因為 $P_0$ 僅為 $z\,(=x_3)$ 的函數，故 $i=1,2$ 的偏微分為零。

    $$\begin{gather*}
    P(x,y,z,t) &\overset{\text{let}}{=}& P_0(z) + p(x,y,z,t) \\
    \frac{\partial P_0}{\partial x_i} &=& \frac{\mathrm{d}P_0}{\mathrm{d}z}\,\delta_{i3} \\
    &\overset{\text{靜力平衡}}{=}& -\rho_0\, g\, \delta_{i3}
    \end{gather*}$$

    * $P$ : 總壓力 (total pressure) $[\text{Pa}]$，純量場，即【已知 1】中的 $P$
    * $P_0(z)$ : 靜力平衡基本態壓力 (hydrostatic base-state pressure) $[\text{Pa}]$，僅依賴高度 $z$
    * $p(x,y,z,t)$ : 擾動壓力 (perturbation pressure) $[\text{Pa}]$，純量場；其雷諾分解見【假設 1(b)】
    * $\delta_{i3}$ : Kronecker delta，見【已知 2(b-1)】

* **【假設 4】 旋轉座標 (Rotating Frame)** ：在隨地球轉動的座標系中，動量方程式右側須補上科氏加速度。

  $$(-2\,\boldsymbol{\Omega} \times \mathbf{u})_i \overset{\text{LC}}{=} -2\,\varepsilon_{ijk}\,\Omega_j\, u_k$$

  * $\boldsymbol{\Omega}$ : 地球自轉角速度向量 (Earth's rotation vector) $[\text{s}^{-1}]$
  * $\Omega_j$ : 其第 $j$ 分量 $[\text{s}^{-1}]$
  * 外積展開依【已知 2(a-2)】

* **【定義 1】 紊流動能 (Turbulent Kinetic Energy, TKE)** ：單位質量的擾動動能。

  $$e \overset{\text{def}}{=} \frac{1}{2}\overline{u'_i u'_i}$$

  * $e$ : 單位質量紊流動能 (TKE per unit mass) $[\text{m}^2\cdot\text{s}^{-2}]$

* **【定義 2】 黏滯耗散率 (Turbulent Dissipation Rate)** ：擾動動能轉為熱能的速率，恆非負。

  $$\varepsilon \overset{\text{def}}{=} \nu\,\overline{\frac{\partial u'_i}{\partial x_j}\frac{\partial u'_i}{\partial x_j}} \;\ge\; 0$$

  * $\varepsilon$ : 耗散率 (dissipation rate) $[\text{m}^2\cdot\text{s}^{-3}]$（**無指標**，勿與 Levi-Civita 的 $\varepsilon_{ijk}$ 混淆）

* **【推導 1】 浮力項 (Buoyancy Term)** ：把【已知 1】的重力項與壓力梯度項，在 Boussinesq 近似下合併。

  $$\begin{gather*}
  -g\,\delta_{i3} - \frac{1}{\rho}\frac{\partial P}{\partial x_i}
  &\overset{\text{假設 3(a),假設 3(c)}}{=}& -g\,\delta_{i3} - \frac{1}{\rho_0 + \tilde{\rho}}\frac{\partial (P_0 + p)}{\partial x_i} \\
  &\overset{\text{假設 3(a)}}{\approx}& -g\,\delta_{i3} - \frac{1}{\rho_0}\Bigl(1 - \frac{\tilde{\rho}}{\rho_0}\Bigr)\frac{\partial P_0}{\partial x_i} - \frac{1}{\rho_0}\frac{\partial p}{\partial x_i} \\
  &\overset{\text{假設 3(c)}}{=}& -g\,\delta_{i3} - \frac{1}{\rho_0}\Bigl(1 - \frac{\tilde{\rho}}{\rho_0}\Bigr)\bigl(-\rho_0\, g\,\delta_{i3}\bigr) - \frac{1}{\rho_0}\frac{\partial p}{\partial x_i} \\
  &=& -g\,\delta_{i3} + g\,\delta_{i3} - \frac{\tilde{\rho}}{\rho_0} g\,\delta_{i3} - \frac{1}{\rho_0}\frac{\partial p}{\partial x_i} \\
  &=& -\frac{g\,\tilde{\rho}}{\rho_0}\,\delta_{i3} - \frac{1}{\rho_0}\frac{\partial p}{\partial x_i}
  \end{gather*}$$

  * 第二列丟棄的是 $O(\tilde{\rho}^2/\rho_0^2)$ 的高階小量（【假設 3(a)】的 $|\tilde{\rho}| \ll \rho_0$）。

* **【推導 2】 工作方程式 (Working Equation)** ：把【推導 1】的浮力項與【假設 4】的科氏力代回【已知 1】，即本推導真正的起點。

  $$\begin{gather*}
  \frac{\partial u_i}{\partial t} + u_j \frac{\partial u_i}{\partial x_j}
  &\overset{\text{已知 1,假設 4}}{=}& -g\,\delta_{i3} - \frac{1}{\rho}\frac{\partial P}{\partial x_i} - 2\varepsilon_{ijk}\Omega_j u_k + \frac{\mu}{\rho}\frac{\partial^2 u_i}{\partial x_j \partial x_j} \\
  &\overset{\text{推導 1}}{=}& -\frac{1}{\rho_0}\frac{\partial p}{\partial x_i} - \frac{g\,\tilde{\rho}}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j u_k + \frac{\mu}{\rho}\frac{\partial^2 u_i}{\partial x_j \partial x_j} \\
  &\overset{\text{假設 3(b)}}{=}& -\frac{1}{\rho_0}\frac{\partial p}{\partial x_i} - \frac{g\,\tilde{\rho}}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j u_k + \nu \frac{\partial^2 u_i}{\partial x_j \partial x_j}
  \end{gather*}$$

* **【推導 3】 平均動量方程式 (Mean Momentum Equation)** ：對【推導 2】的工作方程式整條取系集平均。(a)(b) 是逐項的中間結果，(c) 是本卡片要交付的方程式。

  * **(a) 平流項取平均**

    $$\begin{gather*}
    \overline{u_j \frac{\partial u_i}{\partial x_j}}
    &\overset{\text{chain rule}}{=}& \overline{\frac{\partial}{\partial x_j}\Bigl[u_i u_j\Bigr] - u_i \frac{\partial u_j}{\partial x_j}} \\
    &\overset{\text{假設 2(a)}}{=}& \overline{\frac{\partial}{\partial x_j}\Bigl[u_i u_j\Bigr]} \\
    &\overset{\text{已知 3(d)}}{=}& \frac{\partial}{\partial x_j}\overline{u_i u_j} \\
    &\overset{\text{假設 1(a)}}{=}& \frac{\partial}{\partial x_j}\overline{\Bigl[(\bar{u}_i + u'_i)(\bar{u}_j + u'_j)\Bigr]} \\
    &\overset{\text{已知 3(a)}}{=}& \frac{\partial}{\partial x_j}\Bigl[\overline{\bar{u}_i \bar{u}_j} + \overline{\bar{u}_i u'_j} + \overline{u'_i \bar{u}_j} + \overline{u'_i u'_j}\Bigr] \\
    &\overset{\text{已知 3(c)}}{=}& \frac{\partial}{\partial x_j}\Bigl[\bar{u}_i \bar{u}_j + \bar{u}_i \overline{u'_j} + \bar{u}_j \overline{u'_i} + \overline{u'_i u'_j}\Bigr] \\
    &\overset{\text{已知 3(b)}}{=}& \frac{\partial}{\partial x_j}\Bigl[\bar{u}_i \bar{u}_j\Bigr] + \frac{\partial \overline{u'_i u'_j}}{\partial x_j} \\
    &\overset{\text{chain rule}}{=}& \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j} + \bar{u}_i \frac{\partial \bar{u}_j}{\partial x_j} + \frac{\partial \overline{u'_i u'_j}}{\partial x_j} \\
    &\overset{\text{假設 2(b)}}{=}& \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \overline{u'_i u'_j}}{\partial x_j}
    \end{gather*}$$

  * **(b) 其餘各項取平均**

    $$\begin{gather*}
    \overline{\frac{\partial u_i}{\partial t}} &\overset{\text{已知 3(e)}}{=}& \frac{\partial \bar{u}_i}{\partial t} \\
    \overline{\frac{\partial p}{\partial x_i}} &\overset{\text{已知 3(d)}}{=}& \frac{\partial \bar{p}}{\partial x_i} \\
    \overline{\tilde{\rho}} &\overset{\text{假設 1(c)}}{=}& \bar{\rho} \\
    \overline{u_k} &\overset{\text{假設 1(a),已知 3(b)}}{=}& \bar{u}_k \\
    \overline{\frac{\partial^2 u_i}{\partial x_j \partial x_j}} &\overset{\text{已知 3(d)}}{=}& \frac{\partial^2 \bar{u}_i}{\partial x_j \partial x_j}
    \end{gather*}$$

  * **(c) 平均動量方程式**

    $$\begin{gather*}
    \overline{\frac{\partial u_i}{\partial t}} + \overline{u_j \frac{\partial u_i}{\partial x_j}}
    &\overset{\text{推導 2,已知 3(a)}}{=}& -\frac{1}{\rho_0}\overline{\frac{\partial p}{\partial x_i}} - \frac{g}{\rho_0}\overline{\tilde{\rho}}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j \overline{u_k} + \nu\, \overline{\frac{\partial^2 u_i}{\partial x_j \partial x_j}} \\
    \frac{\partial \bar{u}_i}{\partial t} + \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \overline{u'_i u'_j}}{\partial x_j}
    &\overset{\text{推導 3(a),推導 3(b)}}{=}& -\frac{1}{\rho_0}\frac{\partial \bar{p}}{\partial x_i} - \frac{g\,\bar{\rho}}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j \bar{u}_k + \nu \frac{\partial^2 \bar{u}_i}{\partial x_j \partial x_j}
    \end{gather*}$$

* **【推導 4】 科氏力項歸零 (Coriolis Term Vanishes)** ：反對稱張量 $\varepsilon_{ijk}$ 與對稱張量 $u'_i u'_k$ 的雙重縮併必為零。這是本推導最關鍵的一步。

  $$\begin{gather*}
  \varepsilon_{ijk}\, u'_i u'_k &\overset{\text{啞指標改名 } i \leftrightarrow k}{=}& \varepsilon_{kji}\, u'_k u'_i \\
  &\overset{\text{已知 2(a-1)}}{=}& -\varepsilon_{ijk}\, u'_k u'_i \\
  &=& -\varepsilon_{ijk}\, u'_i u'_k \\
  2\,\varepsilon_{ijk}\, u'_i u'_k &=& 0 \\
  \varepsilon_{ijk}\, u'_i u'_k &=& 0
  \end{gather*}$$

  * **物理意義**：科氏力恆與速度垂直，故對流體**不做功**，不能生成或消滅 TKE。

* **【推導 5】 黏滯項拆分 (Splitting the Viscous Term)** ：把 $u'_i$ 乘上黏滯項後的平均，拆成「黏滯擴散」與「耗散」。

  $$\begin{gather*}
  \nu\, u'_i \frac{\partial^2 u'_i}{\partial x_j \partial x_j}
  &\overset{\text{chain rule}}{=}& \nu\,\frac{\partial}{\partial x_j}\Bigl[u'_i \frac{\partial u'_i}{\partial x_j}\Bigr] - \nu\,\frac{\partial u'_i}{\partial x_j}\frac{\partial u'_i}{\partial x_j} \\
  &\overset{\text{chain rule}}{=}& \nu\,\frac{\partial}{\partial x_j}\frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i\Bigr] - \nu\,\frac{\partial u'_i}{\partial x_j}\frac{\partial u'_i}{\partial x_j} \\
  \nu\,\overline{u'_i \frac{\partial^2 u'_i}{\partial x_j \partial x_j}}
  &\overset{\text{已知 3(d)}}{=}& \nu\,\frac{\partial^2}{\partial x_j \partial x_j}\overline{\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} - \nu\,\overline{\frac{\partial u'_i}{\partial x_j}\frac{\partial u'_i}{\partial x_j}} \\
  &\overset{\text{定義 1,定義 2}}{=}& \nu\,\frac{\partial^2 e}{\partial x_j \partial x_j} - \varepsilon
  \end{gather*}$$

* **【推導 6】 內積 $u'_i$ 後各項的合併 (Term-by-term Reduction after Dotting with $u'_i$)** ：以下六個小結果供 Step 2 直接引用。

  * **(a) 時間項**

    $$\begin{gather*}
    \overline{u'_i \frac{\partial u'_i}{\partial t}} &\overset{\text{chain rule}}{=}& \overline{\frac{\partial}{\partial t}\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} \\
    &\overset{\text{已知 3(e)}}{=}& \frac{\partial}{\partial t}\overline{\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} \\
    &\overset{\text{定義 1}}{=}& \frac{\partial e}{\partial t}
    \end{gather*}$$

  * **(b) 平均流平流項**

    $$\begin{gather*}
    \overline{\bar{u}_j\, u'_i \frac{\partial u'_i}{\partial x_j}} &\overset{\text{chain rule}}{=}& \overline{\bar{u}_j \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} \\
    &\overset{\text{已知 3(c)}}{=}& \bar{u}_j\, \overline{\frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} \\
    &\overset{\text{已知 3(d)}}{=}& \bar{u}_j \frac{\partial}{\partial x_j}\overline{\Bigl[\frac{1}{2}u'_i u'_i\Bigr]} \\
    &\overset{\text{定義 1}}{=}& \bar{u}_j \frac{\partial e}{\partial x_j}
    \end{gather*}$$

  * **(c) 剪力生成項**

    $$\overline{u'_i u'_j \frac{\partial \bar{u}_i}{\partial x_j}} \overset{\text{已知 3(c)}}{=} \overline{u'_i u'_j}\,\frac{\partial \bar{u}_i}{\partial x_j}$$

  * **(d) 三階動差傳輸項**

    $$\begin{gather*}
    u'_i u'_j \frac{\partial u'_i}{\partial x_j} &\overset{\text{chain rule}}{=}& u'_j \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i\Bigr] \\
    &\overset{\text{chain rule}}{=}& \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i u'_j\Bigr] - \frac{1}{2}u'_i u'_i \frac{\partial u'_j}{\partial x_j} \\
    &\overset{\text{假設 2(c)}}{=}& \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}u'_i u'_i u'_j\Bigr] \\
    \overline{u'_i u'_j \frac{\partial u'_i}{\partial x_j}} &\overset{\text{已知 3(d)}}{=}& \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}\overline{u'_i u'_i u'_j}\Bigr]
    \end{gather*}$$

  * **(e) 雷諾應力散度項歸零**

    $$\begin{gather*}
    \overline{u'_i \frac{\partial \overline{u'_i u'_j}}{\partial x_j}} &\overset{\text{已知 3(c)}}{=}& \frac{\partial \overline{u'_i u'_j}}{\partial x_j}\,\overline{u'_i} \\
    &\overset{\text{已知 3(b)}}{=}& 0
    \end{gather*}$$

  * **(f) 壓力項**

    $$\begin{gather*}
    u'_i \frac{\partial p'}{\partial x_i} &\overset{\text{chain rule}}{=}& \frac{\partial}{\partial x_i}\Bigl[p' u'_i\Bigr] - p' \frac{\partial u'_i}{\partial x_i} \\
    &\overset{\text{假設 2(c)}}{=}& \frac{\partial}{\partial x_i}\Bigl[p' u'_i\Bigr] \\
    \overline{u'_i \frac{\partial p'}{\partial x_i}} &\overset{\text{已知 3(d)}}{=}& \frac{\partial \overline{p' u'_i}}{\partial x_i}
    \end{gather*}$$

+++

## 證明 (Derivation)

### Step 1 proof 擾動動量方程式 (Perturbation Momentum Equation)

從【推導 2】的**工作方程式**出發（第一列），以【假設 1】把全場量展開成「平均 ＋ 擾動」（第二列）；寫下【推導 3(c)】的**平均動量方程式**（第三列）；第二列減第三列，即得**擾動動量方程式**（第四列）。

$$\begin{gather*}
\frac{\partial u_i}{\partial t} + u_j \frac{\partial u_i}{\partial x_j}
&\overset{\text{推導 2}}{=}& -\frac{1}{\rho_0}\frac{\partial p}{\partial x_i} - \frac{g\,\tilde{\rho}}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j u_k + \nu \frac{\partial^2 u_i}{\partial x_j \partial x_j} \\
\frac{\partial \bar{u}_i}{\partial t} + \frac{\partial u'_i}{\partial t} + \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j} + \bar{u}_j \frac{\partial u'_i}{\partial x_j} + u'_j \frac{\partial \bar{u}_i}{\partial x_j} + u'_j \frac{\partial u'_i}{\partial x_j}
&\overset{\text{假設 1}}{=}& -\frac{1}{\rho_0}\frac{\partial (\bar{p} + p')}{\partial x_i} - \frac{g\,(\bar{\rho} + \rho')}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j (\bar{u}_k + u'_k) + \nu \frac{\partial^2 (\bar{u}_i + u'_i)}{\partial x_j \partial x_j} \\
\frac{\partial \bar{u}_i}{\partial t} + \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \overline{u'_i u'_j}}{\partial x_j}
&\overset{\text{推導 3(c)}}{=}& -\frac{1}{\rho_0}\frac{\partial \bar{p}}{\partial x_i} - \frac{g\,\bar{\rho}}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j \bar{u}_k + \nu \frac{\partial^2 \bar{u}_i}{\partial x_j \partial x_j} \\
\frac{\partial u'_i}{\partial t} + \bar{u}_j \frac{\partial u'_i}{\partial x_j} + u'_j \frac{\partial \bar{u}_i}{\partial x_j} + u'_j \frac{\partial u'_i}{\partial x_j} - \frac{\partial \overline{u'_i u'_j}}{\partial x_j}
&\overset{\text{第二列} - \text{第三列}}{=}& -\frac{1}{\rho_0}\frac{\partial p'}{\partial x_i} - \frac{g\,\rho'}{\rho_0}\,\delta_{i3} - 2\varepsilon_{ijk}\Omega_j u'_k + \nu \frac{\partial^2 u'_i}{\partial x_j \partial x_j}
\end{gather*}$$

### Step 2 proof 內積 $u'_i$ 取平均並整理成 TKE 方程式 (Dot with $u'_i$, Average, Rearrange)

把 Step 1 的擾動動量方程式整條乘上 $u'_i$ 再取系集平均，逐項套用【推導 4】【推導 5】【推導 6】，最後移項並把傳輸項收成單一散度。

$$\begin{gather*}
\overline{u'_i \frac{\partial u'_i}{\partial t}} + \overline{\bar{u}_j u'_i \frac{\partial u'_i}{\partial x_j}} + \overline{u'_i u'_j \frac{\partial \bar{u}_i}{\partial x_j}} + \overline{u'_i u'_j \frac{\partial u'_i}{\partial x_j}} - \overline{u'_i \frac{\partial \overline{u'_i u'_j}}{\partial x_j}}
&\overset{\text{Step 1} \times u'_i}{=}& -\frac{1}{\rho_0}\overline{u'_i \frac{\partial p'}{\partial x_i}} - \frac{g}{\rho_0}\delta_{i3}\,\overline{u'_i \rho'} - 2\Omega_j\, \overline{\varepsilon_{ijk} u'_i u'_k} + \nu\, \overline{u'_i \frac{\partial^2 u'_i}{\partial x_j \partial x_j}} \\
\frac{\partial e}{\partial t} + \bar{u}_j \frac{\partial e}{\partial x_j} + \overline{u'_i u'_j}\frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}\overline{u'_i u'_i u'_j}\Bigr] - 0
&\overset{\text{推導 6}}{=}& -\frac{1}{\rho_0}\frac{\partial \overline{p' u'_j}}{\partial x_j} - \frac{g}{\rho_0}\delta_{i3}\,\overline{u'_i \rho'} - 2\Omega_j\, \overline{\varepsilon_{ijk} u'_i u'_k} + \nu\, \overline{u'_i \frac{\partial^2 u'_i}{\partial x_j \partial x_j}} \\
\frac{\partial e}{\partial t} + \bar{u}_j \frac{\partial e}{\partial x_j} + \overline{u'_i u'_j}\frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}\overline{u'_i u'_i u'_j}\Bigr]
&\overset{\text{已知 2(b-2),推導 4,推導 5}}{=}& -\frac{1}{\rho_0}\frac{\partial \overline{p' u'_j}}{\partial x_j} - \frac{g}{\rho_0}\overline{w' \rho'} + \nu \frac{\partial^2 e}{\partial x_j \partial x_j} - \varepsilon \\
\frac{\partial e}{\partial t} + \bar{u}_j \frac{\partial e}{\partial x_j}
&=& -\overline{u'_i u'_j}\frac{\partial \bar{u}_i}{\partial x_j} - \frac{g}{\rho_0}\overline{w' \rho'} - \frac{1}{\rho_0}\frac{\partial \overline{p' u'_j}}{\partial x_j} - \frac{\partial}{\partial x_j}\Bigl[\frac{1}{2}\overline{u'_i u'_i u'_j}\Bigr] + \nu \frac{\partial^2 e}{\partial x_j \partial x_j} - \varepsilon \\
&=& -\overline{u'_i u'_j}\frac{\partial \bar{u}_i}{\partial x_j} - \frac{g}{\rho_0}\overline{w' \rho'} - \frac{\partial}{\partial x_j}\Bigl[\frac{1}{\rho_0}\overline{p' u'_j} + \frac{1}{2}\overline{u'_i u'_i u'_j} - \nu \frac{\partial e}{\partial x_j}\Bigr] - \varepsilon
\end{gather*}$$

即得 **TKE 方程式**：

$$\frac{\partial e}{\partial t} + \bar{u}_j \frac{\partial e}{\partial x_j} = \underbrace{-\overline{u'_i u'_j}\frac{\partial \bar{u}_i}{\partial x_j}}_{M} \underbrace{- \frac{g}{\rho_0}\overline{w' \rho'}}_{B} \underbrace{- \frac{\partial}{\partial x_j}\Bigl[\frac{1}{\rho_0}\overline{p' u'_j} + \frac{1}{2}\overline{u'_i u'_i u'_j} - \nu \frac{\partial e}{\partial x_j}\Bigr]}_{T} \underbrace{- \varepsilon}_{\text{耗散}}$$

+++

## 向量形式對照與物理意義 (Vector Form & Physical Meaning)

### 向量形式 (vector form)

指標形式利於推導，向量形式利於理解幾何與物理。逐項翻譯：

$$\frac{\partial e}{\partial t} + (\bar{\mathbf{u}} \cdot \nabla) e = -\bigl(\overline{\mathbf{u}' \otimes \mathbf{u}'}\bigr) : \nabla \bar{\mathbf{u}} - \frac{g}{\rho_0}\overline{w' \rho'} - \nabla \cdot \Bigl(\frac{1}{\rho_0}\overline{p' \mathbf{u}'} + \frac{1}{2}\overline{|\mathbf{u}'|^2\, \mathbf{u}'} - \nu \nabla e\Bigr) - \varepsilon$$

* $\otimes$ : 張量積 (outer product)，$\overline{\mathbf{u}' \otimes \mathbf{u}'}$ 即雷諾應力矩陣 (Reynolds stress)
* $:$ : 雙點積 (double dot product)，兩矩陣對應元素相乘後全部加總

### 各項物理意義

| 項 | 指標形式 | 名稱 | 物理意義 |
|---|---|---|---|
| $\dfrac{\partial e}{\partial t} + \bar{u}_j \dfrac{\partial e}{\partial x_j}$ | — | 全導數 (material derivative) | TKE 沿平均流的時間變化率 + 平均平流 |
| $M$ | $-\overline{u'_i u'_j}\dfrac{\partial \bar{u}_i}{\partial x_j}$ | 剪力生成 (shear production) | 平均流動能經雷諾應力轉換給亂流；有風切就有亂流 |
| $B$ | $-\dfrac{g}{\rho_0}\overline{w' \rho'}$ | 浮力生成／消耗 (buoyancy production) | 輕的往上（$\overline{w'\rho'}<0$）則 $B>0$ 產生亂流；穩定層結則消耗亂流 |
| $T$ | $-\dfrac{\partial}{\partial x_j}\Bigl[\cdots\Bigr]$ | 傳輸 (transport) | 壓力做功 + 三階動差傳輸 + 黏滯擴散；**散度形式**故只重分布、不產生淨能量 |
| $\varepsilon$ | $\nu\,\overline{\dfrac{\partial u'_i}{\partial x_j}\dfrac{\partial u'_i}{\partial x_j}}$ | 黏滯耗散 (dissipation) | 動能轉為熱能，恆 $\ge 0$，是 TKE 的最終匯 |

* 科氏力項在 Step 2 已由【推導 4】歸零，**不出現**在 TKE 方程式中——科氏力不做功。
* 若定義浮力 $b' \overset{\text{def}}{=} -\dfrac{g\rho'}{\rho_0}$，則浮力項可寫成更常見的 $B = \overline{w' b'}$。

+++

## 參考資料

* [Boundary Layer Meteorology — TKE](https://boundary-layer-meteo.github.io/lectures/7_tke.html)
* [動量方程式 (Navier–Stokes) — Advanced Atmospheric Dynamics, week1](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#momentum-equation-navier-stokes)
* [Levi-Civita symbol 主筆記](./Levi-Civita_symbol.ipynb)
