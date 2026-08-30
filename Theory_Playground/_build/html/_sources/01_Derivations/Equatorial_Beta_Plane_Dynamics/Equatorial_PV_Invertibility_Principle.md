# Equatorial PV Invertibility Principle (赤道位渦可逆性原理)

+++

## 證明目標:

**端點③的前半。** 把 [位渦距平的定義](Equatorial_PV_Equation_and_Beta_y_Source.md) 從「$q$ 由流場算出來」
翻轉成「流場由 $q$ 解出來」。關鍵是補上一條把質量場 $\phi$ 與風場 $\psi$ 綁在一起的**平衡關係**。

* (a) 用流函數改寫位渦定義（**含 $\psi$ 與 $\phi$ 兩個未知數，還不可解**）：

$$\nabla^{2}\psi + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} = q$$

* (b) **★ 樞紐一步** —— 線性平衡關係加上「$\beta y$ 緩變」的假設，退化成一條**局地**（非積分型）的關係：

$$\phi = \beta y\,\psi$$

* (c) 把 (b) 代進 (a)，得到**只含 $\psi$ 與 $q$ 的橢圓型偏微分方程式** —— 這就是可逆性原理：

$$\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} = q$$

* (d) 經垂直分離、隨波定常化與緯向傅立葉轉換後，(c) 化成對 $\hat{y}$ 的常微分方程式：

$$\epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m - m^{2}\hat{\psi}_m = a^{2}\hat{q}_m$$

* 註：(a)–(d) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(6.1)$–$(6.3)$。
* 註：**(b) 是整個赤道可逆性原理的樞紐。** 它把中緯度的地轉關係 $\phi = f\psi$ 直接搬到赤道 $\beta$ 平面（$f \to \beta y$）。有了它，知道 $q$ 就能解出 $\psi$，進而由 $\left(u_\psi, v_\psi\right) = \left(-\partial\psi/\partial y,\ \partial\psi/\partial x\right)$ 與 $\phi = \beta y\psi$ 還原全部平衡場。
* 註：(d) 左端的算符 $\dfrac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}$ **正是** [Hermite 函數的諧振子本徵值](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md)【證明 (a)】那一個。下一篇 [Hermite 轉換解](Hermite_Transform_Solution_of_Invertibility.md) 就靠這件事把整條方程式壓成一行除法。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [位渦距平的定義 (Definition of the PV anomaly)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#a-proof-emergence-of-the-potential-vorticity-anomaly)：** 赤道 $\beta$ 平面上的位渦距平：相對渦度加上「以 $\beta y$ 加權的層結項」。因為權重正比於 $y$，赤道上這一項自動消失 ─ 這是整條 MJO 推導鏈的物理引擎。（已於本庫 [Equatorial PV Equation and the Beta-y Source](Equatorial_PV_Equation_and_Beta_y_Source.md)【證明 (a)】完整證明，此處直接引用。）

  $$q = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z}$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【已知 2】 [線性平衡關係 (Linear balance relation)](https://glossary.ametsoc.org/wiki/Balance_equation)：** 從水平動量方程式取散度、丟掉加速度與非線性項後得到的診斷關係。（標準結果，此處直接引用。）

  $$\nabla\cdot\left(\beta y\,\nabla\psi\right) = \nabla^{2}\phi$$

  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\nabla^{2}$ : 水平拉普拉斯算符 (Horizontal Laplacian) $[\text{m}^{-2}]$，$\nabla^{2} = \dfrac{\partial^{2}}{\partial x^{2}} + \dfrac{\partial^{2}}{\partial y^{2}}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$

* **【已知 3】 [垂直結構方程式與分離形式 (Vertical structure equation and the separable forms)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Vertical_Structure_Equation_in_Log_Pressure.html#a-proof-eigenvalue-of-the-first-vertical-internal-mode)：** 垂直本徵問題與它的分離形式：分離常數 $\lambda$ 同時等於 $\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}$ 與 $\frac{R\Gamma}{\bar{c}^{2}}$（後者即等效重力波速的來源），而 $\psi,\ \phi,\ q$ 三者都掛在同一個 $Z(z)$ 上，因此垂直方向可以整個約掉。（已於本庫 [Vertical Structure Equation in Log-Pressure](Vertical_Structure_Equation_in_Log_Pressure.md) 與 [Physical Field Recovery](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)【推導 1】完整證明，此處直接引用。）

  * (a) 垂直結構方程式：

    $$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\lambda Z, \qquad \lambda = \frac{\pi^{2}}{z_T^{2}} + \frac{1}{4} = \frac{R\Gamma}{\bar{c}^{2}}$$

  * (b) $\psi,\ \phi,\ q$ 都掛在同一個 $Z(z)$ 上：

    $$\left(\psi,\ \phi,\ q\right) = \left(\hat{\psi},\ \hat{\phi},\ \hat{q}\right)Z(z)$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $\hat{\psi},\ \hat{q}$ : 流函數與位渦的水平結構函數 (Horizontal structure functions of the streamfunction and the PV) $[\text{m}^{2}\cdot\text{s}^{-1}],\ [\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$

* **【已知 4】 [隨波定常化與緯向傅立葉轉換 (Steadiness in the translating frame and the zonal Fourier transform)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#a-proof-derivative-replacement-in-the-translating-frame)：** 兩步把緯向微分變成代數乘法：先換到隨熱源移動的座標 $\xi = x - ct$ 使場變定常，再對 $\xi$ 做傅立葉轉換 ─ 於是 $\partial/\partial x$ 整個變成 $im/a$。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (a)(b)】完整證明，此處直接引用。）

  $$\frac{\partial}{\partial x} \to \frac{\partial}{\partial \xi} \to \frac{im}{a}, \qquad \xi = x - ct$$

  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$

* **【已知 5】 [Lamb 參數與無因次經向座標 (Lamb's parameter and the dimensionless meridional coordinate)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#assumptions-preliminaries)：** 把經向座標無因次化的兩個量：$\epsilon$ 量度旋轉相對於層結的強弱，$\hat{y}$ 以赤道變形半徑為長度單位 ─ 本篇靠它把可逆性方程改寫成標準的量子諧振子形式。（已於本庫 [Energy Inner Product and the Skew-Hermitian Operator](Energy_Inner_Product_and_Skew_Hermitian_Operator.md)【定義 2】給出，此處直接引用。）

  $$\epsilon = \frac{4\Omega^{2}a^{2}}{\bar{c}^{2}}, \qquad \hat{y} = \left(\frac{\beta}{\bar{c}}\right)^{1/2}y$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【假設 1】 流場以旋轉部分為主 (The flow is dominated by its rotational part)：** 水平風場用流函數表示，忽略輻散部分

  $$\left(u_\psi,\ v_\psi\right) = \left(-\frac{\partial \psi}{\partial y},\ \frac{\partial \psi}{\partial x}\right)$$

  * $u_\psi,\ v_\psi$ : 旋轉風的兩個分量 (Rotational wind components) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$

* **【假設 2】 $\beta y$ 緩變 (Slowly varying $\beta y$)：** 在【已知 2】中把 $\beta y$ 當成可以穿過拉普拉斯算符的量

  $$\nabla\cdot\left(\beta y\,\nabla\psi\right) \approx \nabla^{2}\left(\beta y\,\psi\right)$$

  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * 註：**這是全篇唯一一條「有代價」的假設**。嚴格展開時 $\nabla^{2}\left(\beta y\psi\right) = \beta y\nabla^{2}\psi + 2\beta\dfrac{\partial\psi}{\partial y}$，而 $\nabla\cdot\left(\beta y\nabla\psi\right) = \beta y\nabla^{2}\psi + \beta\dfrac{\partial\psi}{\partial y}$ —— 兩者差一個 $\beta\dfrac{\partial\psi}{\partial y}$。當 $\psi$ 的經向尺度遠小於 $y$ 本身時（即遠離赤道），該項相對可忽略。

* **【假設 3】 無窮遠處的邊界條件 (Boundary condition at infinity)：** 用來從【推導 2】的拉普拉斯方程挑出唯一解

  $$\lim_{\left|y\right| \to \infty}\left(\phi - \beta y\,\psi\right) = 0$$

  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$

* **【假設 4】 可逆性原理的邊界條件 (Boundary conditions for the invertibility principle)：** 【證明 (c)】的橢圓方程配上這兩條才構成完整的定解問題

  * (a) 經向：

    $$\lim_{\left|y\right| \to \infty}\psi = 0$$

  * (b) 垂直：

    $$\left.\frac{\partial \psi}{\partial z}\right|_{z = 0} = \left.\frac{\partial \psi}{\partial z}\right|_{z = z_T} = 0$$

  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * 註：這一張卡片**不以 `\overset` 形式出現在下方的【證明】中** —— 邊界條件不是某個等號的依據，而是讓【證明 (c)】的橢圓型方程「解存在且唯一」的定解條件。它真正被用到是在下一篇 [Hermite 轉換解](Hermite_Transform_Solution_of_Invertibility.md)：(a) 保證 Hermite 展開合法（$\mathcal{H}_n$ 在無窮遠處歸零），(b) 保證垂直結構取 $Z(z)$（見 [垂直結構方程式](Vertical_Structure_Equation_in_Log_Pressure.md)【假設 1】的同一條件）。

* **【推導 1】 相對渦度的流函數形式 (Streamfunction form of the relative vorticity)：** 把旋轉流用流函數表示後，相對渦度就退化成流函數的拉普拉斯 ─ 這一步把「兩個風速分量」換成「一個純量場」，是後面位渦可逆性能寫成單一橢圓方程的關鍵。

  $$\begin{gather*}
  \frac{\partial v_\psi}{\partial x} - \frac{\partial u_\psi}{\partial y} &\overset{\text{假設 1}}{=}& \frac{\partial}{\partial x}\left[\frac{\partial \psi}{\partial x}\right] - \frac{\partial}{\partial y}\left[-\frac{\partial \psi}{\partial y}\right] \\
  &=& \frac{\partial^{2}\psi}{\partial x^{2}} + \frac{\partial^{2}\psi}{\partial y^{2}} \\
  &\overset{\text{已知 2}}{=}& \nabla^{2}\psi
  \end{gather*}$$

  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【推導 2】 平衡關係的局地化 (Localizing the balance relation)：** 【假設 2】把積分型的線性平衡關係變成一個拉普拉斯方程

  $$\begin{gather*}
  \nabla^{2}\phi &\overset{\text{已知 2}}{=}& \nabla\cdot\left(\beta y\,\nabla\psi\right) \\
  \nabla^{2}\phi &\overset{\text{假設 2}}{\approx}& \nabla^{2}\left(\beta y\,\psi\right) \\
  \nabla^{2}\left(\phi - \beta y\,\psi\right) &=& 0
  \end{gather*}$$

  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$

* **【推導 3】 垂直算符作用在分離形式上 (The vertical operator acting on the separable form)：** 把垂直算符作用在可分離的 $\psi = \hat{\psi}Z(z)$ 上：垂直結構函數滿足的本徵方程把整個算符收成一個常數 $-\lambda$，於是三維問題降成純水平的二維問題。

  $$\begin{gather*}
  \left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} &\overset{\text{已知 3(b)}}{=}& \hat{\psi}\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} \\
  &\overset{\text{已知 3(a)}}{=}& -\lambda\,\hat{\psi}\,Z
  \end{gather*}$$

  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction of the rotational flow) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\hat{\psi},\ \hat{q}$ : 流函數與位渦的水平結構函數 (Horizontal structure functions of the streamfunction and the PV) $[\text{m}^{2}\cdot\text{s}^{-1}],\ [\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$

* **【推導 4】 經向座標的無因次化 (Nondimensionalizing the meridional coordinate)：** 兩個關鍵的換算

  * (a) 二階導數：

    $$\begin{gather*}
    \frac{d^{2}}{dy^{2}} &\overset{\text{已知 5}}{=}& \frac{\beta}{\bar{c}}\frac{d^{2}}{d\hat{y}^{2}}
    \end{gather*}$$

  * (b) $\beta^{2}y^{2}$ 的組合：

    $$\begin{gather*}
    \frac{\beta^{2}y^{2}}{\bar{c}^{2}} &\overset{\text{已知 5}}{=}& \frac{\beta^{2}}{\bar{c}^{2}}\cdot\frac{\bar{c}}{\beta}\hat{y}^{2} \\
    &=& \frac{\beta}{\bar{c}}\hat{y}^{2}
    \end{gather*}$$

  * (c) 前因子的化簡：

    $$\begin{gather*}
    \frac{\beta a^{2}}{\bar{c}} &\overset{\text{已知 1}}{=}& \frac{2\Omega a}{\bar{c}} \\
    &\overset{\text{已知 5}}{=}& \epsilon^{1/2}
    \end{gather*}$$

  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$

+++

## 證明:

### (a) proof 位渦定義的流函數形式 (Streamfunction form of the PV definition)

$$\begin{gather*}
q &\overset{\text{已知 1}}{=}& \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} \\
&\overset{\text{推導 1}}{=}& \nabla^{2}\psi + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z}
\end{gather*}$$

### (b) proof 局地平衡關係 (Local balance relation)

【推導 2】說 $\phi - \beta y\psi$ 是調和函數；調和函數在無窮遠處歸零（【假設 3】），由最大值原理只能恆為零。

$$\begin{gather*}
\nabla^{2}\left(\phi - \beta y\,\psi\right) &\overset{\text{推導 2}}{=}& 0 \\
\phi - \beta y\,\psi &\overset{\text{假設 3}}{=}& 0 \\
\phi &=& \beta y\,\psi
\end{gather*}$$

### (c) proof 可逆性原理 (Invertibility principle)

把【證明 (b)】代進【證明 (a)】，方程式只剩 $\psi$ 一個未知數；配上【假設 4】的邊界條件即構成完整的定解問題。

$$\begin{gather*}
q &\overset{\text{證明 (a)}}{=}& \nabla^{2}\psi + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} \\
&\overset{\text{證明 (b)}}{=}& \nabla^{2}\psi + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \left(\beta y\,\psi\right)}{\partial z} \\
&=& \nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z}
\end{gather*}$$

### (d) proof 譜空間的可逆性原理 (Invertibility principle in spectral space)

三步化簡：垂直分離（【推導 3】）、緯向傅立葉（【已知 4】）、經向無因次化（【推導 4】）。

$$\begin{gather*}
\hat{q}\,Z &\overset{\text{證明 (c),已知 3(b)}}{=}& \left[\frac{\partial^{2}\hat{\psi}}{\partial x^{2}} + \frac{\partial^{2}\hat{\psi}}{\partial y^{2}}\right]Z + \frac{\beta^{2}y^{2}}{R\Gamma}\left(-\lambda\,\hat{\psi}\,Z\right) \\
\hat{q} &\overset{\text{推導 3,已知 3(a)}}{=}& \frac{\partial^{2}\hat{\psi}}{\partial x^{2}} + \frac{\partial^{2}\hat{\psi}}{\partial y^{2}} - \frac{\beta^{2}y^{2}}{\bar{c}^{2}}\hat{\psi} \\
\hat{q}_m &\overset{\text{已知 4}}{=}& -\frac{m^{2}}{a^{2}}\hat{\psi}_m + \frac{d^{2}\hat{\psi}_m}{dy^{2}} - \frac{\beta^{2}y^{2}}{\bar{c}^{2}}\hat{\psi}_m \\
\hat{q}_m &\overset{\text{推導 4(a)(b)}}{=}& -\frac{m^{2}}{a^{2}}\hat{\psi}_m + \frac{\beta}{\bar{c}}\left[\frac{d^{2}\hat{\psi}_m}{d\hat{y}^{2}} - \hat{y}^{2}\hat{\psi}_m\right] \\
a^{2}\hat{q}_m &=& \frac{\beta a^{2}}{\bar{c}}\left[\frac{d^{2}\hat{\psi}_m}{d\hat{y}^{2}} - \hat{y}^{2}\hat{\psi}_m\right] - m^{2}\hat{\psi}_m \\
a^{2}\hat{q}_m &\overset{\text{推導 4(c)}}{=}& \epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m - m^{2}\hat{\psi}_m
\end{gather*}$$

+++

## 物理解釋

### 「可逆」到底可逆了什麼

【證明 (a)】的方向是 **流場 $\Rightarrow$ PV**：給定 $u, v, \phi$，$q$ 算得出來。這沒什麼稀奇。

有價值的是**反方向**。但【證明 (a)】裡有 $\psi$ 與 $\phi$ **兩個**未知數，一條方程式解不出兩個未知數。【證明 (b)】補上的 $\phi = \beta y\psi$ 就是那條缺的方程式。

補上之後，【證明 (c)】變成一個**只含 $\psi$ 與 $q$ 的橢圓型偏微分方程**。橢圓型的意義是：給定右端 $q$ 與邊界條件，解**存在且唯一**。於是：

$$q \xrightarrow{\ \text{解橢圓方程}\ } \psi \xrightarrow{\ \left(u_\psi, v_\psi\right) = \left(-\psi_y,\ \psi_x\right)\ } \text{旋轉風} \quad\text{且}\quad \psi \xrightarrow{\ \phi = \beta y\psi\ } \text{質量場}$$

**只要知道 PV，整個平衡流場就還原得出來。**

### $\phi = \beta y\psi$ 為什麼是樞紐

中緯度 $f$ 平面上，地轉關係是 $\phi = f_0\psi$ —— 一個乘常數的**局地**關係。赤道 $\beta$ 平面上 $f = \beta y$ 不是常數，嚴格的線性平衡關係 $\nabla\cdot\left(\beta y\nabla\psi\right) = \nabla^{2}\phi$ 是一個**橢圓方程**，$\phi$ 與 $\psi$ 之間是**非局地**的。

【假設 2】的「$\beta y$ 緩變」把非局地關係**壓成局地**的 $\phi = \beta y\psi$。這一步買到的是「代入即可」的方便，付出的代價是漏掉 $\beta\dfrac{\partial\psi}{\partial y}$ 那一項 —— 而該項在赤道附近（$y \to 0$、$\beta y \to 0$）相對最大。

**換句話說：可逆性原理在赤道正上方最不準。** 這與 [Kelvin 波零 PV](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)【證明 (d)】的失敗區域**重疊**，兩者一起造成論文 §6 觀察到的唯一破綻：「原始方程模式中赤道上的緯向氣壓梯度力，在可逆性原理的解裡完全沒有被重現」。

### 諧振子算符為什麼會出現在這裡

【證明 (d)】的左端

$$\epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right) - m^{2}$$

那個 $\dfrac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}$ **正是**量子諧振子的算符，也正是 [Hermite 函數](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md)【證明 (a)】那個本徵值為 $-(2n+1)$ 的算符。

它從哪裡來？兩塊拼起來的：

* $\dfrac{d^{2}}{d\hat{y}^{2}}$ —— 來自拉普拉斯算符的經向部分（渦度）；
* $-\hat{y}^{2}$ —— 來自 $\beta^{2}y^{2}$，也就是**平衡關係 $\phi = \beta y\psi$ 用了兩次**（一次在 $q$ 的定義裡、一次在代入時）。

**$\beta y$ 出現兩次是這個算符成為諧振子的唯一原因。** 中緯度 $f$ 平面上對應的是 $f_0^{2}$ 常數，算符會退化成 Helmholtz 型（$\nabla^{2} - \text{const}$），本徵函數是三角函數而非 Hermite 函數。

下一篇 [Hermite 轉換解](Hermite_Transform_Solution_of_Invertibility.md) 就靠這件事，把整條橢圓方程在譜空間壓成**一行除法**。
