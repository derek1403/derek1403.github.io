# Energy Inner Product and the Skew-Hermitian Operator (能量內積與算符的反厄米性)

+++

## 證明目標:

整套正規模態展開的**合法性**都押在這一篇。要證的是：算符 $\mathcal{L}$ 相對於一個
「由總能量原理定出來的」內積是**反厄米**的，因此它的本徵函數構成完備正交基底。

* (a) 線性系統的總能量原理：

$$\frac{d\mathcal{E}}{dt} = -2\alpha\mathcal{E} + \mathcal{G}$$

  其中

$$\mathcal{E} = \iiint\frac{1}{2}\left[u^{2} + v^{2} + \frac{1}{R\Gamma}\left(\frac{\partial \phi}{\partial z}\right)^{2}\right]e^{-z}\,dx\,dy\,dz,
\qquad
\mathcal{G} = \iiint\frac{1}{c_p\Gamma}\frac{\partial \phi}{\partial z}\,Q\,e^{-z}\,dx\,dy\,dz$$

* (b) 隨波定常時，總能量原理退化為「耗散＝生成」的平衡：

$$2\alpha\mathcal{E} = \mathcal{G}$$

* (c) **★ 內積 $(4.8)$ 第三分量的權重 $1/\bar{c}^{2}$ 不是隨手挑的** —— 把 (a) 的 $\mathcal{E}$ 做垂直分離，該權重會**自動**掉出來：

$$\mathcal{E} = \frac{I_Z}{2}\iint\left[\hat{u}^{2} + \hat{v}^{2} + \frac{1}{\bar{c}^{2}}\hat{\phi}^{2}\right]dx\,dy,
\qquad I_Z \overset{\text{def}}{=} \int_0^{z_T}Z^{2}e^{-z}\,dz$$

* (d) **★ 相對於該內積，算符 $\mathcal{L}$ 是反厄米的：**

$$\mathcal{L}^{\dagger} = -\mathcal{L}$$

* (e) 由 (d) 推出的兩個紅利 —— 本徵值為**純虛數**、相異本徵值的本徵函數**互相正交**：

$$\nu_{mnr} \in \mathbb{R}, \qquad \left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) = 0 \quad \left(\nu_{mnr} \neq \nu_{mn'r'}\right)$$

* 註：(a)(b) 是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(2.2)$–$(2.3)$，(c)(d) 對應 $(4.8)$ 與其後的敘述。
* 註：論文只說內積 $(4.8)$ 是「由總能量原理**暗示 (suggested)**」出來的。本篇的【證明 (c)】把這句話**升級成嚴格推導** —— 權重 $1/\bar{c}^{2}$ 是垂直積分恆等式 $\int Z'^{2}e^{-z}dz = \lambda\int Z^{2}e^{-z}dz$（【推導 5】）的必然結果。
* 註：反厄米性的證明手法已在 Advanced Atmospheric Dynamics 的 [project1_3](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project1/project1_3.html) 對另一個算符完整示範過，內積的正定性見 [project1_4](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project1/project1_4.html)。本篇只是把同一套手法套在 Schubert 的 $\mathcal{L}$ 上。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對數氣壓座標下的線性化原始方程組 (Log-pressure linearized primitive equations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 對數氣壓座標下、繞靜止基本態線性化後的五條方程式：兩條水平動量方程、靜力方程、連續方程式與熱力學方程式。本篇要證的能量守恆與算符反厄米性都建立在它們之上。（已於本庫 [Log-Pressure Linearized Primitive Equations](Log_Pressure_Linearized_Primitive_Equations.md) 完整證明，此處直接引用。）

  * (a) 緯向動量方程式：

    $$\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} = -\alpha u$$

  * (b) 經向動量方程式：

    $$\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} = -\alpha v$$

  * (c) 靜力方程式：

    $$\frac{\partial \phi}{\partial z} = RT$$

  * (d) 連續方程式：

    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = w$$

  * (e) 熱力學方程式：

    $$\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p}$$

  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【已知 2】 [垂直結構方程式與分離形式 (Vertical structure equation and the separable forms)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Separation_into_Horizontal_Structure_System.html#assumptions-preliminaries)：** 垂直方向的本徵問題與它所決定的分離形式：$Z$ 滿足帶邊界條件的二階常微分方程，而 $u,\ v,\ \phi$ 掛在 $Z$ 上、$T,\ w,\ Q$ 掛在 $Z'$ 上 ─ 這兩組不同的垂直結構是靜力方程式逼出來的，不是湊的。（已於本庫 [Vertical Structure Equation in Log-Pressure](Vertical_Structure_Equation_in_Log_Pressure.md) 與 [Separation into the Horizontal Structure System](Separation_into_Horizontal_Structure_System.md) 完整證明，此處直接引用。）

  * (a) 垂直結構方程式：

    $$\frac{d^{2}Z}{dz^{2}} - \frac{dZ}{dz} = -\lambda Z$$

  * (b) 邊界條件：

    $$\left.\frac{dZ}{dz}\right|_{z = 0} = \left.\frac{dZ}{dz}\right|_{z = z_T} = 0$$

  * (c) 分離形式：

    $$\left(u,\ v,\ \phi\right) = \left(\hat{u},\ \hat{v},\ \hat{\phi}\right)Z(z), \qquad \left(T,\ w,\ Q\right) = \left(\hat{T},\ \hat{w},\ \hat{Q}\right)Z'(z)$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda = \dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$

* **【已知 3】 [線性算符 $\mathcal{L}$ (Linear operator $\mathcal{L}$)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#e-proof-vector-form)：** 把水平結構方程組寫成 $\partial_t\hat{\boldsymbol{\eta}} = -\mathcal{L}\hat{\boldsymbol{\eta}}$ 之後的 $3 \times 3$ 算符：對角線全為零，非對角元由科氏項 $\beta y$、緯向波數 $im/a$ 與經向微分 $d/dy$ 構成 ─ 本篇要證的正是它在能量內積下反厄米。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (e)】完整證明，此處直接引用。）

  $$\mathcal{L} = \begin{pmatrix} 0 & -\beta y & \dfrac{im}{a} \cr \beta y & 0 & \dfrac{d}{dy} \cr \bar{c}^{2}\dfrac{im}{a} & \bar{c}^{2}\dfrac{d}{dy} & 0 \end{pmatrix}$$

  * $\mathcal{L}$ : 水平結構的線性算符 (Linear operator) $[\text{s}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【已知 4】 [分部積分 (Integration by parts)](https://dlmf.nist.gov/1.4#E33)：** 把微分從一個因子轉移到另一個因子的標準手段，代價是多出一個邊界項 ─ 證明反厄米性時，正是靠它把 $d/dy$ 搬過內積，再用【假設 1】的邊界條件把邊界項清成零。（標準結果，此處直接引用。）

  $$\int_{p}^{q} F\,\frac{dG}{ds}\,ds = \left[F\,G\right]_{p}^{q} - \int_{p}^{q} G\,\frac{dF}{ds}\,ds$$

  * $F,\ G$ : 任意可微函數 (Arbitrary differentiable functions) $[\text{依應用而定}]$
  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$
  * $p,\ q$ : 積分上下限 (Limits of integration) $[\text{依應用而定}]$

* **【假設 1】 求解區域與邊界條件 (Domain and boundary conditions)：** 三個方向各自的邊界處理，本篇所有「邊界項為零」都出自這一張卡片

  * (a) 緯向週期，週期為 $2\pi a$：

    $$\left.\left(\cdot\right)\right|_{x = -\pi a} = \left.\left(\cdot\right)\right|_{x = \pi a}$$

  * (b) 經向無限，場在無窮遠處歸零（赤道捕捉）：

    $$\lim_{\left|y\right| \to \infty}\left(u,\ v,\ \phi\right) = 0$$

  * (c) 垂直方向剛蓋：

    $$\left.w\right|_{z = 0} = \left.w\right|_{z = z_T} = 0$$

  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$

* **【假設 2】 隨波定常 (Steadiness in the translating frame)：** 在以速度 $c$ 東移的參考系中，總能量不隨時間變化

  $$\frac{d\mathcal{E}}{dt} = 0$$

  * $\mathcal{E}$ : 總能量 (Total energy) $[\text{m}^{4}\cdot\text{s}^{-2}]$
  * $t$ : 時間 (Time) $[\text{s}]$

* **【假設 3】 本徵函數的赤道捕捉性 (Equatorial trapping of the eigenfunctions)：** 內積中出現的所有分量在 $\hat{y} \to \pm\infty$ 時歸零，因此【證明 (d)】的分部積分不留邊界項

  $$\lim_{\left|\hat{y}\right| \to \infty}\left(f_1,\ f_2,\ f_3\right) = \lim_{\left|\hat{y}\right| \to \infty}\left(g_1,\ g_2,\ g_3\right) = 0$$

  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【定義 1】 總能量與生成項 (Total energy and generation term)：** 動能加上以 $e^{-z}$ 加權的可用位能

  * (a) 總能量：

    $$\mathcal{E} \overset{\text{def}}{=} \iiint\frac{1}{2}\left[u^{2} + v^{2} + \frac{1}{R\Gamma}\left(\frac{\partial \phi}{\partial z}\right)^{2}\right]e^{-z}\,dx\,dy\,dz$$

  * (b) 生成項：

    $$\mathcal{G} \overset{\text{def}}{=} \iiint\frac{1}{c_p\Gamma}\frac{\partial \phi}{\partial z}\,Q\,e^{-z}\,dx\,dy\,dz$$

  * $\mathcal{E}$ : 總能量 (Total energy) $[\text{m}^{4}\cdot\text{s}^{-2}]$
  * $\mathcal{G}$ : 非絕熱生成項 (Diabatic generation term) $[\text{m}^{4}\cdot\text{s}^{-3}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * 註：權重 $e^{-z}$ 就是密度 —— 由 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【推導 1】，$P = p_0e^{-z}$，而等溫近似下 $\rho \propto P$。所以 $\mathcal{E}$ 是「質量加權」的能量。

* **【定義 2】 無因次經向座標與 Lamb 參數 (Dimensionless meridional coordinate and Lamb's parameter)：** 兩個把赤道波問題無因次化的量：Lamb 參數 $\epsilon$ 量度旋轉相對於層結的強弱（$\epsilon$ 越大，旋轉越主導）；由它縮放出來的 $\hat{y}$ 則把赤道變形半徑當成長度單位，使後續的 Hermite 函數不帶任何物理參數。

  * (a) Lamb 參數：

    $$\epsilon \overset{\text{def}}{=} \frac{4\Omega^{2}a^{2}}{\bar{c}^{2}}$$

  * (b) 無因次經向座標：

    $$\begin{gather*}
    \hat{y} &\overset{\text{def}}{=}& \left(\frac{\beta}{\bar{c}}\right)^{1/2}y \\
    &\overset{\text{已知 1}}{=}& \left(\frac{2\Omega}{a\bar{c}}\right)^{1/2}y \\
    &\overset{\text{定義 2(a)}}{=}& \epsilon^{1/4}\frac{y}{a}
    \end{gather*}$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【定義 3】 能量內積 (Energy inner product)：** 三分量向量函數的內積，第三分量帶著 $1/\bar{c}^{2}$ 的權重

  $$\left(\mathbf{f},\ \mathbf{g}\right) \overset{\text{def}}{=} \int_{-\infty}^{\infty}\left(f_1g_1^{*} + f_2g_2^{*} + \frac{1}{\bar{c}^{2}}f_3g_3^{*}\right)d\hat{y}$$

  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$
  * $\left(\cdot\right)^{*}$ : 複數共軛 (Complex conjugate) $[\text{無單位}]$
  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * 註：這張卡片是**定義**，不是宣稱。它為什麼該長這樣（尤其那個 $1/\bar{c}^{2}$），由【證明 (c)】回答。

* **【定義 4】 伴隨算符 (Adjoint operator)：** 相對於【定義 3】的內積所定義的伴隨

  $$\left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) \overset{\text{def}}{=} \left(\mathbf{f},\ \mathcal{L}^{\dagger}\mathbf{g}\right)$$

  * $\mathcal{L}^{\dagger}$ : $\mathcal{L}$ 的伴隨算符 (Adjoint of $\mathcal{L}$) $[\text{s}^{-1}]$
  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$

* **【定義 5】 位勢通量積分 (Geopotential flux integral)：** 壓力（位勢）對流場作功的總積分，先取個名字讓【證明 (a)】不被它撐爆

  $$\mathcal{F} \overset{\text{def}}{=} \iiint\left[u\frac{\partial \phi}{\partial x} + v\frac{\partial \phi}{\partial y} + w\frac{\partial \phi}{\partial z}\right]e^{-z}\,dx\,dy\,dz$$

  * $\mathcal{F}$ : 位勢通量積分 (Geopotential flux integral) $[\text{m}^{4}\cdot\text{s}^{-3}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【推導 1】 動能方程式 (Kinetic energy equation)：** 用 $u$ 乘【已知 1】(a)、用 $v$ 乘【已知 1】(b) 再相加，科氏項對消

  $$\begin{gather*}
  -\alpha u^{2} - \alpha v^{2} &\overset{\text{已知 1(a)(b)}}{=}& u\left[\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x}\right] + v\left[\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y}\right] \\
  &=& u\frac{\partial u}{\partial t} + v\frac{\partial v}{\partial t} - \beta y\,uv + \beta y\,uv + u\frac{\partial \phi}{\partial x} + v\frac{\partial \phi}{\partial y} \\
  &=& \frac{\partial}{\partial t}\left[\frac{u^{2} + v^{2}}{2}\right] + u\frac{\partial \phi}{\partial x} + v\frac{\partial \phi}{\partial y}
  \end{gather*}$$

  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * 註：科氏項 $\mp\beta y\,uv$ 精確對消 —— 科氏力**不做功**，這是能量原理成立的第一個關鍵。

* **【推導 2】 位能方程式 (Available potential energy equation)：** 用 $\dfrac{R}{\Gamma}T$ 乘【已知 1】(e)

  $$\begin{gather*}
  \frac{R}{\Gamma}T\left[-\alpha T + \frac{Q}{c_p}\right] &\overset{\text{已知 1(e)}}{=}& \frac{R}{\Gamma}T\left[\frac{\partial T}{\partial t} + \Gamma w\right] \\
  -\alpha\frac{R}{\Gamma}T^{2} + \frac{R\,T\,Q}{\Gamma c_p} &=& \frac{\partial}{\partial t}\left[\frac{R\,T^{2}}{2\Gamma}\right] + R\,T\,w
  \end{gather*}$$

  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$

* **【推導 3】 位能密度的兩種寫法 (Two forms of the potential energy density)：** 靜力方程式讓 $T$ 與 $\partial\phi/\partial z$ 可以互換

  $$\begin{gather*}
  \frac{R\,T^{2}}{\Gamma} &\overset{\text{已知 1(c)}}{=}& \frac{R}{\Gamma}\left[\frac{1}{R}\frac{\partial \phi}{\partial z}\right]^{2} \\
  \frac{R\,T^{2}}{\Gamma} &=& \frac{1}{R\Gamma}\left(\frac{\partial \phi}{\partial z}\right)^{2} \\
  R\,T\,w &\overset{\text{已知 1(c)}}{=}& w\frac{\partial \phi}{\partial z}
  \end{gather*}$$

  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$

* **【推導 4】 位勢通量項的總積分為零 (Vanishing of the total geopotential flux)：** 這是能量原理成立的第二個關鍵 —— 壓力作功只是在系統內部搬運能量，總量不變

  * (a) 用乘積律拆成散度減去輻散項，再用連續方程式：

    $$\begin{gather*}
    u\frac{\partial \phi}{\partial x} + v\frac{\partial \phi}{\partial y} + w\frac{\partial \phi}{\partial z}
    &=& \frac{\partial \left(\phi u\right)}{\partial x} + \frac{\partial \left(\phi v\right)}{\partial y} + \frac{\partial \left(\phi w\right)}{\partial z} - \phi\left[\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}\right] \\
    &\overset{\text{已知 1(d)}}{=}& \frac{\partial \left(\phi u\right)}{\partial x} + \frac{\partial \left(\phi v\right)}{\partial y} + \frac{\partial \left(\phi w\right)}{\partial z} - \phi\,w
    \end{gather*}$$

  * (b) 水平兩項的積分為零（緯向週期、經向衰減）：

    $$\iiint\left[\frac{\partial \left(\phi u\right)}{\partial x} + \frac{\partial \left(\phi v\right)}{\partial y}\right]e^{-z}\,dx\,dy\,dz \overset{\text{假設 1(a)(b)}}{=} 0$$

  * (c) 垂直項用分部積分，邊界項被剛蓋殺掉，剩下的恰好抵掉 (a) 的 $-\phi w$：

    $$\begin{gather*}
    \iiint \frac{\partial \left(\phi w\right)}{\partial z}e^{-z}\,dx\,dy\,dz &\overset{\text{已知 4}}{=}& \iint\left\{\left[e^{-z}\phi w\right]_{0}^{z_T} + \int_{0}^{z_T}\phi\,w\,e^{-z}\,dz\right\}dx\,dy \\
    &\overset{\text{假設 1(c)}}{=}& \iiint \phi\,w\,e^{-z}\,dx\,dy\,dz
    \end{gather*}$$

  * (d) 三項合起來：

    $$\begin{gather*}
    \mathcal{F} &\overset{\text{定義 5,推導 4(a)(b)(c)}}{=}& \iiint \phi\,w\,e^{-z}\,dV - \iiint \phi\,w\,e^{-z}\,dV \\
    &=& 0
    \end{gather*}$$

  * $dV$ : 體積元 $dx\,dy\,dz$ 的簡寫 (Volume element) $[\text{m}^{2}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $\mathcal{F}$ : 位勢通量積分 (Geopotential flux integral) $[\text{m}^{4}\cdot\text{s}^{-3}]$

* **【推導 5】 垂直積分恆等式 (Vertical integral identity)：** $Z'$ 的加權平方積分恰為 $Z$ 的 $\lambda$ 倍 —— 這是【證明 (c)】的全部關鍵

  $$\begin{gather*}
  -\lambda\int_{0}^{z_T}Z^{2}e^{-z}\,dz &\overset{\text{已知 2(a)}}{=}& \int_{0}^{z_T}Z\left[\frac{d^{2}Z}{dz^{2}} - \frac{dZ}{dz}\right]e^{-z}\,dz \\
  -\lambda\int_{0}^{z_T}Z^{2}e^{-z}\,dz &=& \int_{0}^{z_T}Z\,\frac{d}{dz}\left[e^{-z}\frac{dZ}{dz}\right]dz \\
  -\lambda\int_{0}^{z_T}Z^{2}e^{-z}\,dz &\overset{\text{已知 4}}{=}& \left[Z\,e^{-z}\frac{dZ}{dz}\right]_{0}^{z_T} - \int_{0}^{z_T}\left(\frac{dZ}{dz}\right)^{2}e^{-z}\,dz \\
  -\lambda\int_{0}^{z_T}Z^{2}e^{-z}\,dz &\overset{\text{已知 2(b)}}{=}& -\int_{0}^{z_T}\left(\frac{dZ}{dz}\right)^{2}e^{-z}\,dz \\
  \int_{0}^{z_T}\left(\frac{dZ}{dz}\right)^{2}e^{-z}\,dz &=& \lambda\int_{0}^{z_T}Z^{2}e^{-z}\,dz
  \end{gather*}$$

  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda = \dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * 註：第一列到第二列用到 $\dfrac{d}{dz}\left[e^{-z}\dfrac{dZ}{dz}\right] = e^{-z}\left[\dfrac{d^{2}Z}{dz^{2}} - \dfrac{dZ}{dz}\right]$ —— 也就是說，**$e^{-z}$ 正是讓垂直算子變成自伴形式的積分因子**。這與本庫 [Sturm–Liouville 正交性](../Differential_Equations/Sturm_Liouville_Orthogonality.md)【定義 1】的 $p(z)$ 是同一件事。

* **【推導 6】 $\mathcal{L}\mathbf{f}$ 與 $\mathbf{g}$ 的內積展開 (Expansion of the inner product)：** 把【已知 3】代進【定義 3】，逐項寫開

  $$\begin{gather*}
  \left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) &\overset{\text{定義 3,已知 3}}{=}& \int_{-\infty}^{\infty}\left[\left(-\beta y f_2 + \frac{im}{a}f_3\right)g_1^{*} + \left(\beta y f_1 + \frac{df_3}{dy}\right)g_2^{*} + \frac{1}{\bar{c}^{2}}\left(\bar{c}^{2}\frac{im}{a}f_1 + \bar{c}^{2}\frac{df_2}{dy}\right)g_3^{*}\right]d\hat{y} \\
  &=& \int_{-\infty}^{\infty}\left[-\beta y f_2g_1^{*} + \beta y f_1g_2^{*} + \frac{im}{a}f_3g_1^{*} + \frac{im}{a}f_1g_3^{*} + \frac{df_3}{dy}g_2^{*} + \frac{df_2}{dy}g_3^{*}\right]d\hat{y}
  \end{gather*}$$

  * $\mathcal{L}$ : 水平結構的線性算符 (Linear operator) $[\text{s}^{-1}]$
  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【推導 7】 $\mathbf{f}$ 與 $\mathcal{L}\mathbf{g}$ 的內積展開 (Expansion of the conjugate inner product)：** 同樣代入，但注意 $\left(\mathcal{L}\mathbf{g}\right)^{*}$ 會把 $im/a$ 變號

  $$\begin{gather*}
  -\left(\mathbf{f},\ \mathcal{L}\mathbf{g}\right) &\overset{\text{定義 3,已知 3}}{=}& -\int_{-\infty}^{\infty}\left[f_1\left(-\beta y g_2^{*} - \frac{im}{a}g_3^{*}\right) + f_2\left(\beta y g_1^{*} + \frac{dg_3^{*}}{dy}\right) + \frac{1}{\bar{c}^{2}}f_3\left(-\bar{c}^{2}\frac{im}{a}g_1^{*} + \bar{c}^{2}\frac{dg_2^{*}}{dy}\right)\right]d\hat{y} \\
  &=& \int_{-\infty}^{\infty}\left[\beta y f_1g_2^{*} - \beta y f_2g_1^{*} + \frac{im}{a}f_1g_3^{*} + \frac{im}{a}f_3g_1^{*} - f_2\frac{dg_3^{*}}{dy} - f_3\frac{dg_2^{*}}{dy}\right]d\hat{y}
  \end{gather*}$$

  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$
  * $\mathcal{L}$ : 水平結構的線性算符 (Linear operator) $[\text{s}^{-1}]$
  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【推導 8】 微分項的差為全微分 (The derivative terms differ by a total derivative)：** 【推導 6】與【推導 7】只差在微分項，兩者相減後恰好整成全微分

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\left[\frac{df_3}{dy}g_2^{*} + f_3\frac{dg_2^{*}}{dy} + \frac{df_2}{dy}g_3^{*} + f_2\frac{dg_3^{*}}{dy}\right]d\hat{y}
  &=& \int_{-\infty}^{\infty}\frac{d}{dy}\left[f_3g_2^{*} + f_2g_3^{*}\right]d\hat{y} \\
  &=& \left(\frac{\beta}{\bar{c}}\right)^{1/2}\left[f_3g_2^{*} + f_2g_3^{*}\right]_{-\infty}^{\infty} \\
  &\overset{\text{假設 3}}{=}& 0
  \end{gather*}$$

  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c}^{2} = R\Gamma/\lambda \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$
  * 註：第二列用到【定義 2】(b) 的 $\hat{y} = \left(\beta/\bar{c}\right)^{1/2}y$，故 $\dfrac{d}{dy} = \left(\dfrac{\beta}{\bar{c}}\right)^{1/2}\dfrac{d}{d\hat{y}}$，積分後只剩邊界值乘上這個常數。

+++

## 證明:

### (a) proof 總能量原理 (Total energy principle)

把【推導 1】與【推導 2】相加，乘上 $e^{-z}$ 後對全域積分；通量項被【推導 4】整個殺掉，剩下的依【定義 1】收攏。

$$\begin{gather*}
\frac{d\mathcal{E}}{dt} &\overset{\text{定義 1(a),推導 3}}{=}& \iiint\frac{\partial}{\partial t}\left[\frac{u^{2} + v^{2}}{2} + \frac{R\,T^{2}}{2\Gamma}\right]e^{-z}\,dV \\
&\overset{\text{推導 1,推導 2,推導 3,定義 5}}{=}& -\alpha\iiint\left[u^{2} + v^{2} + \frac{R\,T^{2}}{\Gamma}\right]e^{-z}\,dV + \iiint\frac{R\,T\,Q}{\Gamma c_p}e^{-z}\,dV - \mathcal{F} \\
&\overset{\text{推導 3,定義 1(a)(b)}}{=}& -2\alpha\mathcal{E} + \mathcal{G} - \mathcal{F} \\
&\overset{\text{推導 4(d)}}{=}& -2\alpha\mathcal{E} + \mathcal{G}
\end{gather*}$$

### (b) proof 定常時的能量平衡 (Energy balance in the steady state)

$$\begin{gather*}
0 &\overset{\text{假設 2}}{=}& \frac{d\mathcal{E}}{dt} \\
0 &\overset{\text{證明 (a)}}{=}& -2\alpha\mathcal{E} + \mathcal{G} \\
2\alpha\mathcal{E} &=& \mathcal{G}
\end{gather*}$$

### (c) proof 內積權重 $1/\bar{c}^{2}$ 的來源 (Origin of the $1/\bar{c}^{2}$ weight)

把【已知 2】(c) 的分離形式代進【定義 1】(a)，垂直積分用【推導 5】換掉，$\lambda/\left(R\Gamma\right)$ 就變成 $1/\bar{c}^{2}$。

$$\begin{gather*}
\mathcal{E} &\overset{\text{定義 1(a)}}{=}& \iiint\frac{1}{2}\left[u^{2} + v^{2} + \frac{1}{R\Gamma}\left(\frac{\partial \phi}{\partial z}\right)^{2}\right]e^{-z}\,dV \\
&\overset{\text{已知 2(c)}}{=}& \iint\frac{1}{2}\left[\left(\hat{u}^{2} + \hat{v}^{2}\right)\int_{0}^{z_T}Z^{2}e^{-z}\,dz + \frac{\hat{\phi}^{2}}{R\Gamma}\int_{0}^{z_T}\left(\frac{dZ}{dz}\right)^{2}e^{-z}\,dz\right]dx\,dy \\
&\overset{\text{推導 5}}{=}& \iint\frac{1}{2}\left[\left(\hat{u}^{2} + \hat{v}^{2}\right)\int_{0}^{z_T}Z^{2}e^{-z}\,dz + \frac{\lambda\,\hat{\phi}^{2}}{R\Gamma}\int_{0}^{z_T}Z^{2}e^{-z}\,dz\right]dx\,dy \\
&\overset{\text{已知 3}}{=}& \frac{1}{2}\left[\int_{0}^{z_T}Z^{2}e^{-z}\,dz\right]\iint\left[\hat{u}^{2} + \hat{v}^{2} + \frac{1}{\bar{c}^{2}}\hat{\phi}^{2}\right]dx\,dy
\end{gather*}$$

### (d) proof 算符的反厄米性 (Skew-Hermiticity of the operator)

【推導 6】與【推導 7】的前四項逐項相同，剩下的微分項之差被【推導 8】證明為零。

$$\begin{gather*}
\left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) + \left(\mathbf{f},\ \mathcal{L}\mathbf{g}\right)
&\overset{\text{推導 6,推導 7}}{=}& \int_{-\infty}^{\infty}\left[\frac{df_3}{dy}g_2^{*} + \frac{df_2}{dy}g_3^{*} + f_2\frac{dg_3^{*}}{dy} + f_3\frac{dg_2^{*}}{dy}\right]d\hat{y} \\
\left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) + \left(\mathbf{f},\ \mathcal{L}\mathbf{g}\right) &\overset{\text{推導 8}}{=}& 0 \\
\left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) &=& -\left(\mathbf{f},\ \mathcal{L}\mathbf{g}\right) \\
\left(\mathcal{L}\mathbf{f},\ \mathbf{g}\right) &\overset{\text{定義 4}}{=}& \left(\mathbf{f},\ \mathcal{L}^{\dagger}\mathbf{g}\right) \\
\mathcal{L}^{\dagger} &=& -\mathcal{L}
\end{gather*}$$

### (e) proof 本徵值為純虛數且本徵函數正交 (Pure-imaginary eigenvalues and orthogonal eigenfunctions)

* **本徵值：** 令 $\mathcal{L}\mathbf{K} = i\nu\mathbf{K}$，對同一個 $\mathbf{K}$ 取內積並用【證明 (d)】。

$$\begin{gather*}
i\nu\left(\mathbf{K},\ \mathbf{K}\right) &\overset{\text{let}}{=}& \left(\mathcal{L}\mathbf{K},\ \mathbf{K}\right) \\
i\nu\left(\mathbf{K},\ \mathbf{K}\right) &\overset{\text{證明 (d)}}{=}& -\left(\mathbf{K},\ \mathcal{L}\mathbf{K}\right) \\
i\nu\left(\mathbf{K},\ \mathbf{K}\right) &\overset{\text{定義 3}}{=}& -\left(i\nu\right)^{*}\left(\mathbf{K},\ \mathbf{K}\right) \\
i\nu &=& -\left(i\nu\right)^{*} \\
i\nu &=& i\nu^{*} \\
\nu &=& \nu^{*}
\end{gather*}$$

* **正交性：** 取兩個對應到相異本徵值的本徵函數。

$$\begin{gather*}
i\nu_{mnr}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) &\overset{\text{let}}{=}& \left(\mathcal{L}\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) \\
i\nu_{mnr}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) &\overset{\text{證明 (d)}}{=}& -\left(\mathbf{K}_{mnr},\ \mathcal{L}\mathbf{K}_{mn'r'}\right) \\
i\nu_{mnr}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) &\overset{\text{定義 3}}{=}& -\left(i\nu_{mn'r'}\right)^{*}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) \\
i\nu_{mnr}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) &=& i\nu_{mn'r'}\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) \\
0 &=& i\left(\nu_{mnr} - \nu_{mn'r'}\right)\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) \\
0 &=& \left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right)
\end{gather*}$$

+++

## 結構解釋

### 這一篇為什麼一定要獨立成篇

因為**後面每一步都押在它上面**：

* [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md) 的正交歸一 $(4.17)$ —— 靠【證明 (e)】的正交性。
* [受迫解](Forced_Response_of_Equatorial_Modes.md) 的一行除法 $(4.21)$ —— 靠【證明 (d)】把 $\left(\mathcal{L}\hat{\boldsymbol{\eta}},\ \mathbf{K}\right)$ 翻成 $i\nu\hat{\eta}$。
* 頻散關係 $(4.10)$ 的根全為實數 —— 靠【證明 (e)】的 $\nu \in \mathbb{R}$（無成長、無衰減，符合線性無耗散波動的物理）。

若 $\mathcal{L}$ 不是反厄米的，本徵函數不必正交、不必完備，整套正規模態展開就沒有立足點。

### 內積的第三個權重是「算」出來的，不是「猜」出來的

論文只寫「the inner product $(4.8)$ is suggested by the total energy principle」。【證明 (c)】把這句話補完：

$$\underbrace{\frac{1}{R\Gamma}\left(\frac{\partial \phi}{\partial z}\right)^{2}}_{\text{三維位能密度}}
\quad\xrightarrow{\ \text{垂直積分}\ }\quad
\underbrace{\frac{\lambda}{R\Gamma}\hat{\phi}^{2}}_{\text{二維位能密度}}
= \underbrace{\frac{1}{\bar{c}^{2}}\hat{\phi}^{2}}_{\text{內積第三項}}$$

中間那一步靠的就是【推導 5】的 $\int Z'^{2}e^{-z}dz = \lambda\int Z^{2}e^{-z}dz$。

所以：**只要挑了「總能量」當內積，$1/\bar{c}^{2}$ 就沒有選擇餘地。** 反過來說，若隨手把第三項的權重取成 $1$，$\mathcal{L}$ 就**不是**反厄米的（【推導 6】【推導 7】的第三列會湊不起來），整套方法立刻崩潰。

### 兩個「剛好對消」各自對應什麼物理

【證明 (a)】能成立，全靠兩處精確對消：

| 對消 | 出處 | 物理意義 |
|---|---|---|
| $-\beta y\,uv + \beta y\,uv = 0$ | 【推導 1】 | **科氏力不做功**（它永遠垂直於速度） |
| $\iiint\phi w\,e^{-z}dV - \iiint\phi w\,e^{-z}dV = 0$ | 【推導 4】(d) | **壓力作功只在系統內搬運能量**，總量守恆 |

第二個對消特別值得看：它把「$-\phi\left(\nabla\cdot\mathbf{u}\right)$」（連續方程式貢獻的 $-\phi w$）與「垂直分部積分產生的 $+\phi w$」抵掉。**若剛蓋條件 $w\left(0\right) = w\left(z_T\right) = 0$ 不成立，邊界會有能量進出，$(2.2)$ 就不再是封閉的能量原理。**

### 反厄米 vs. 厄米：為什麼是「反」

厄米算符（$\mathcal{L}^{\dagger} = \mathcal{L}$）的本徵值是**實數**，對應到量子力學的可觀測量。

反厄米算符（$\mathcal{L}^{\dagger} = -\mathcal{L}$）的本徵值是**純虛數**。而本系統的時間演化是 $\dfrac{\partial \hat{\boldsymbol{\eta}}}{\partial t} = -\mathcal{L}\hat{\boldsymbol{\eta}}$，解為 $e^{-i\nu t}$ —— 純虛的本徵值 $i\nu$ 給出**純振盪、不成長不衰減**的解。

這正是無耗散線性波動該有的行為。系統真正的衰減來自另一處：【證明 (a)】的 $-2\alpha\mathcal{E}$，也就是 Rayleigh 摩擦與 Newtonian 冷卻 —— 那一項不在 $\mathcal{L}$ 裡，而是 [淺水系統](Fourier_Transform_to_Shallow_Water_System.md)【證明 (e)】那個對角的 $\left(\alpha - imc/a\right)$ 的實部。
