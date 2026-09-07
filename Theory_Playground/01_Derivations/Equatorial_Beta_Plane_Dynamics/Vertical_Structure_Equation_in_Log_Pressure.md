# Vertical Structure Equation in Log-Pressure (對數氣壓座標下的垂直結構方程式)

+++

## 證明目標:

在剛蓋邊界條件 $Z'(0) = Z'(z_T) = 0$ 之下解出**第一垂直內模態**的結構函數。

* (a) 第一垂直內模態的本徵值為 $\dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}$，垂直結構方程式因此寫成：

$$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)Z$$

* (b) 歸一化後的結構函數：

$$Z(z) = \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1/2}e^{\left(z - z_m\right)/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right]$$

* (c) 其導數（$T,\ w,\ Q$ 三個變數之後就掛在這個函數上）：

$$Z'(z) = \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{\left(z - z_m\right)/2}\sin\left(\frac{\pi z}{z_T}\right)$$

* (d) $Z'$ 取極大值的高度 $z_m$ 由下式決定，且該歸一化恰使 $Z'(z_m) = 1$：

$$\frac{\pi z_m}{z_T} = \pi + \tan^{-1}\left(-\frac{2\pi}{z_T}\right), \qquad Z'(z_m) = 1$$

* (e) 代入 $z_T \approx 1.619$ 的數值結果：

$$z_m \approx 0.5803\,z_T$$

其中

* $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
* $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
* $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
* $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
* $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$，$z_T \approx 1.619$
* $z_m$ : $Z$ 對 $z$ 的微分 $\dfrac{dZ}{dz}$（即 $Z'$）取極大值的高度 (Height where $dZ/dz$ is maximum) $[\text{無單位}]$
* 註：(a)–(d) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(3.1)$–$(3.3)$。
* 註：本篇與本庫 [垂直結構方程式（Boussinesq 版）](../Atmospheric_Dynamics/Vertical_Structure_Equation.md) 是**同一套 Sturm–Liouville 手法在不同座標下的兩個實例** —— 那裡的算子是 $\dfrac{\partial}{\partial z}\left[\dfrac{1}{N^{2}}\dfrac{\partial}{\partial z}\right]$，這裡是 $\left(\dfrac{d}{dz} - 1\right)\dfrac{d}{dz}$。差別全部來自「對數氣壓座標帶著密度指數遞減」這一件事。
* 註：為什麼「只留第一內模態」是合理的？論文的證據是觀測：Johnson and Ciesielski (2000) 針對西太平洋暖池所算的 $120$ 天平均加熱率剖面 $Q/c_p$，其**形狀與 $Z'(z)$ 幾乎重合**（原論文 Fig. 1）。本篇只做數學，不重複那個觀測論證。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對數氣壓座標下的線性化原始方程組 (Log-pressure linearized primitive equations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 本篇只用到方程組裡的兩件事：連續方程式（水平輻散與垂直運動的平衡，含對數氣壓座標特有的 $-w$ 項），以及對流層上下界的剛蓋條件（$w$ 在 $z = 0$ 與 $z = z_T$ 為零）─ 後者正是垂直結構本徵值被量子化的來源。（已於本庫 Log-Pressure Linearized Primitive Equations 完整證明，此處直接引用。）

  * (a) 連續方程式：

    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w = 0$$

  * (b) 上下邊界的剛蓋條件：

    $$\left.w\right|_{z = 0} = \left.w\right|_{z = z_T} = 0$$

  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【已知 2】 [二階線性常係數常微分方程式的通解 (General solution of a second-order linear ODE with constant coefficients)](https://dlmf.nist.gov/1.13)：** 特徵方程式有一對純虛根 $\pm ik$ 時，通解為正弦與餘弦的線性組合。（標準結果，此處直接引用。）

  $$\frac{d^{2}Y}{dz^{2}} + k^{2}Y = 0 \quad \Longleftrightarrow \quad Y(z) = A\sin\left(kz\right) + B\cos\left(kz\right)$$

  * $Y(z)$ : 待解函數 (Unknown function) $[\text{依應用而定}]$
  * $k$ : 垂直波數 (Vertical wavenumber) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【定義 1】 對流層頂高度 (Tropopause height)：** 模式的上邊界取在 $200 \ \text{mb}$

  $$\begin{gather*}
  z_T &\overset{\text{def}}{=}& \ln\left(\frac{1010}{200}\right) \\
  &\approx& 1.619
  \end{gather*}$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【定義 2】 垂直結構函數與分離常數 (Vertical structure function and separation constant)：** 把三維問題壓成二維的關鍵設定 —— 令 $u, v, \phi$ 的垂直依賴集中在一個函數 $Z(z)$ 上，而 $Z$ 滿足一個帶分離常數 $\lambda$ 的二階本徵值問題

  $$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} \overset{\text{def}}{=} -\lambda\,Z$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' \overset{\text{def}}{=} \dfrac{dZ}{dz}$
  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：這條式子**目前只是一個定義**（我們宣告要找滿足它的 $Z$）。它為什麼非長這樣不可，要到 [水平結構方程組的分離](Separation_into_Horizontal_Structure_System.md)【證明 (d)】才看得出來 —— 那裡連續方程式裡的 $\left(\dfrac{\partial}{\partial z} - 1\right)w$ 必須正比於 $Z$，才能讓整組方程式閉合。
  * 註（撇號的記號慣例）：本推導鏈的撇號 $'$ **一律只表示對 $z$ 微分**，不表示擾動。書寫上分兩種場合：在**推導列**寫 $\dfrac{dZ}{dz}$，讓「對誰微分」一眼可見；在**命名與引用**時寫 $Z'$，以對齊 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(3.3)$ 與 Fig. 1 圖說 —— 兩種寫法完全同義。擾動量為何反而**不**用撇號，見 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【假設 2】末的〈記號慣例〉註。

* **【假設 1】 剛蓋邊界條件 (Rigid-lid boundary conditions)：** 上下邊界不允許垂直運動，而垂直速度的垂直結構取為 $dZ/dz$，故邊界條件落在 $Z$ 的**導數**上

  * (a) 上下邊界的垂直速度為零：

    $$\left.w\right|_{z = 0} = \left.w\right|_{z = z_T} \overset{\text{已知 1(b)}}{=} 0$$

  * (b) 因 $w \propto dZ/dz$（見下方註），(a) 等價於：

    $$\left.\frac{dZ}{dz}\right|_{z = 0} = \left.\frac{dZ}{dz}\right|_{z = z_T} = 0$$

  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * 註：「$w$ 的垂直結構是 $dZ/dz$ 而不是 $Z$」這件事，在本篇是**設定**；它為什麼是被逼出來的，要到 [水平結構方程組的分離](Separation_into_Horizontal_Structure_System.md)【推導 2】才證得出來。本篇不引用該結果，以免循環論證。

* **【假設 2】 只保留第一垂直內模態 (First vertical internal mode only)：** 本徵值問題有可數無窮多組解，本篇只取節點數最少的非平凡解

  $$n = 1$$

  * $n$ : 垂直模態指標 (Vertical mode index) $[\text{無單位}]$

* **【假設 3】 歸一化條件 (Normalization condition)：** 解的整體倍率由「$Z'$ 的極大值為 $1$」固定下來

  $$Z'\left(z_m\right) = 1$$

  * $z_m$ : $Z$ 對 $z$ 的微分 $\dfrac{dZ}{dz}$（即 $Z'$）取極大值的高度 (Height where $dZ/dz$ is maximum) $[\text{無單位}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$

* **【推導 1】 消去一階項的代換 (Substitution removing the first-order term)：** 【定義 2】展開後含有一階導數項，用 $Z = e^{z/2}Y$ 把它消掉，方程式就退化成最單純的簡諧形式

  * (a) 把【定義 2】展開成標準二階式：

    $$\begin{gather*}
    -\lambda Z &\overset{\text{定義 2}}{=}& \left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} \\
    -\lambda Z &=& \frac{d^{2}Z}{dz^{2}} - \frac{dZ}{dz} \\
    \frac{d^{2}Z}{dz^{2}} - \frac{dZ}{dz} + \lambda Z &=& 0
    \end{gather*}$$

  * (b) 代入 $Z = e^{z/2}Y$，一階項與 $\lambda$ 的一部分同時被吃掉：

    $$\begin{gather*}
    0 &\overset{\text{推導 1(a)}}{=}& \frac{d^{2}}{dz^{2}}\left[e^{z/2}Y\right] - \frac{d}{dz}\left[e^{z/2}Y\right] + \lambda\,e^{z/2}Y \\
    0 &=& e^{z/2}\left[\frac{d^{2}Y}{dz^{2}} + \frac{dY}{dz} + \frac{1}{4}Y\right] - e^{z/2}\left[\frac{dY}{dz} + \frac{1}{2}Y\right] + \lambda\,e^{z/2}Y \\
    0 &=& e^{z/2}\left[\frac{d^{2}Y}{dz^{2}} + \left(\lambda - \frac{1}{4}\right)Y\right] \\
    \frac{d^{2}Y}{dz^{2}} + \left(\lambda - \frac{1}{4}\right)Y &=& 0
    \end{gather*}$$

  * $Y(z)$ : 去掉指數包絡後的結構函數 (Structure function with the exponential envelope removed) $[\text{無單位}]$
  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【推導 2】 通解與第一個邊界條件 (General solution and the first boundary condition)：** 【已知 2】給出通解，$z = 0$ 的邊界條件把兩個常數綁成一個

  * (a) 引入垂直波數，套用【已知 2】：

    $$\begin{gather*}
    k^{2} &\overset{\text{let}}{=}& \lambda - \frac{1}{4} \\
    Y &\overset{\text{推導 1(b),已知 2}}{=}& A\sin\left(kz\right) + B\cos\left(kz\right) \\
    Z &\overset{\text{推導 1(b)}}{=}& e^{z/2}\left[A\sin\left(kz\right) + B\cos\left(kz\right)\right]
    \end{gather*}$$

  * (b) 對 $Z$ 微分，指數與三角各貢獻一項：

    $$\begin{gather*}
    \frac{dZ}{dz} &\overset{\text{推導 2(a)}}{=}& \frac{1}{2}e^{z/2}\left[A\sin\left(kz\right) + B\cos\left(kz\right)\right] + e^{z/2}\left[kA\cos\left(kz\right) - kB\sin\left(kz\right)\right] \\
    &=& e^{z/2}\left[\left(\frac{A}{2} - kB\right)\sin\left(kz\right) + \left(\frac{B}{2} + kA\right)\cos\left(kz\right)\right]
    \end{gather*}$$

  * (c) 代入 $z = 0$ 的邊界條件，解出 $B$：

    $$\begin{gather*}
    0 &\overset{\text{假設 1,推導 2(b)}}{=}& \frac{B}{2} + kA \\
    B &=& -2kA
    \end{gather*}$$

  * (d) 把 (c) 代回 (b)，$\cos$ 項整個消失，$Z'$ 變成純正弦：

    $$\begin{gather*}
    \frac{dZ}{dz} &\overset{\text{推導 2(b)(c)}}{=}& e^{z/2}\left[\left(\frac{A}{2} + 2k^{2}A\right)\sin\left(kz\right) + 0\cdot\cos\left(kz\right)\right] \\
    &=& A\left(\frac{1}{2} + 2k^{2}\right)e^{z/2}\sin\left(kz\right) \\
    &\overset{\text{推導 2(a)}}{=}& 2\lambda A\,e^{z/2}\sin\left(kz\right)
    \end{gather*}$$

  * $k$ : 垂直波數 (Vertical wavenumber) $[\text{無單位}]$
  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $Y(z)$ : 去掉指數包絡後的結構函數 (Structure function with the exponential envelope removed) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$

* **【推導 3】 第二個邊界條件與本徵值 (Second boundary condition and the eigenvalue)：** $z = z_T$ 的條件把 $k$ 量子化，第一內模態的本徵值於是確定

  $$\begin{gather*}
  0 &\overset{\text{假設 1,推導 2(d)}}{=}& 2\lambda A\,e^{z_T/2}\sin\left(kz_T\right) \\
  0 &=& \sin\left(kz_T\right) \\
  kz_T &=& n\pi \qquad \left(n = 1, 2, 3, \ldots\right) \\
  k &\overset{\text{假設 2}}{=}& \frac{\pi}{z_T} \\
  \lambda &\overset{\text{推導 2(a)}}{=}& k^{2} + \frac{1}{4} \\
  \lambda &=& \frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}
  \end{gather*}$$

  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $k$ : 垂直波數 (Vertical wavenumber) $[\text{無單位}]$
  * $n$ : 垂直模態指標 (Vertical mode index) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【推導 4】 $Z'$ 極大值的位置 (Location of the maximum of $Z'$)：** 對【推導 2】(d) 再微分一次並令其為零

  $$\begin{gather*}
  0 &\overset{\text{推導 2(d)}}{=}& \frac{d}{dz}\left[2\lambda A\,e^{z/2}\sin\left(kz\right)\right] \\
  0 &=& 2\lambda A\,e^{z/2}\left[\frac{1}{2}\sin\left(kz\right) + k\cos\left(kz\right)\right] \\
  0 &=& \frac{1}{2}\sin\left(kz_m\right) + k\cos\left(kz_m\right) \\
  \tan\left(kz_m\right) &=& -2k \\
  \tan\left(\frac{\pi z_m}{z_T}\right) &\overset{\text{推導 3}}{=}& -\frac{2\pi}{z_T} \\
  \frac{\pi z_m}{z_T} &=& \pi + \tan^{-1}\left(-\frac{2\pi}{z_T}\right)
  \end{gather*}$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$
  * $k$ : 垂直波數 (Vertical wavenumber) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $z_m$ : $Z$ 對 $z$ 的微分 $\dfrac{dZ}{dz}$（即 $Z'$）取極大值的高度 (Height where $dZ/dz$ is maximum) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * 註：最後一步取的是**第二象限**的那個根（$\pi/2 < \pi z_m/z_T < \pi$）。取第一象限的根會落在 $\sin$ 為正、$\cos$ 也為正的區間，對應的是 $Z'$ 的**極小**而非極大；而 $\tan^{-1}$ 的主值域是 $\left(-\pi/2, \pi/2\right)$，故需補上 $\pi$。

* **【推導 5】 $z_m$ 處的三角函數值 (Trigonometric values at $z_m$)：** 由【推導 4】的正切值與第二象限的符號，直接讀出正弦與餘弦

  * (a) 正弦（第二象限為正）：

    $$\begin{gather*}
    \sin\left(\frac{\pi z_m}{z_T}\right) &\overset{\text{推導 4}}{=}& \frac{2\pi}{\left(4\pi^{2} + z_T^{2}\right)^{1/2}} \\
    &=& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{-1/2}
    \end{gather*}$$

  * (b) 餘弦（第二象限為負）：

    $$\cos\left(\frac{\pi z_m}{z_T}\right) \overset{\text{推導 4}}{=} -\frac{z_T}{\left(4\pi^{2} + z_T^{2}\right)^{1/2}}$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $z_m$ : $Z$ 對 $z$ 的微分 $\dfrac{dZ}{dz}$（即 $Z'$）取極大值的高度 (Height where $dZ/dz$ is maximum) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$

* **【推導 6】 歸一化常數 (Normalization constant)：** 用【假設 3】把 $A$ 定下來

  $$\begin{gather*}
  1 &\overset{\text{假設 3,推導 2(d)}}{=}& 2\lambda A\,e^{z_m/2}\sin\left(\frac{\pi z_m}{z_T}\right) \\
  A &=& \frac{e^{-z_m/2}}{2\lambda\,\sin\left(\pi z_m/z_T\right)} \\
  2\lambda A &=& \frac{e^{-z_m/2}}{\sin\left(\pi z_m/z_T\right)} \\
  2\lambda A &\overset{\text{推導 5(a)}}{=}& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{-z_m/2}
  \end{gather*}$$

  * $\lambda$ : 分離常數（本徵值）(Separation constant / eigenvalue) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $z_m$ : $Z$ 對 $z$ 的微分 $\dfrac{dZ}{dz}$（即 $Z'$）取極大值的高度 (Height where $dZ/dz$ is maximum) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$

+++

## 證明:

### (a) proof 第一垂直內模態的本徵值 (Eigenvalue of the first vertical internal mode)

把【推導 3】的本徵值代回【定義 2】即得。

$$\begin{gather*}
\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} &\overset{\text{定義 2}}{=}& -\lambda Z \\
&\overset{\text{推導 3}}{=}& -\left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)Z
\end{gather*}$$

### (b) proof 歸一化的垂直結構函數 (Normalized vertical structure function)

從【推導 2】(a)(c) 的解出發，把 $\cos$ 提出來湊成論文的括號形式，再用【推導 6】代入歸一化常數。

$$\begin{gather*}
Z &\overset{\text{推導 2(a)(c)}}{=}& A\,e^{z/2}\left[\sin\left(kz\right) - 2k\cos\left(kz\right)\right] \\
&\overset{\text{推導 3}}{=}& A\,e^{z/2}\left[\sin\left(\frac{\pi z}{z_T}\right) - \frac{2\pi}{z_T}\cos\left(\frac{\pi z}{z_T}\right)\right] \\
&=& \frac{2\pi A}{z_T}\,e^{z/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right] \\
&\overset{\text{推導 6}}{=}& \frac{2\pi}{z_T}\cdot\frac{1}{2\lambda}\left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{\left(z - z_m\right)/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right] \\
&\overset{\text{推導 3}}{=}& \frac{2\pi}{z_T}\cdot\frac{2z_T^{2}}{4\pi^{2} + z_T^{2}}\cdot\frac{\left(4\pi^{2} + z_T^{2}\right)^{1/2}}{2\pi}\,e^{\left(z - z_m\right)/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right] \\
&=& \frac{2z_T}{\left(4\pi^{2} + z_T^{2}\right)^{1/2}}\,e^{\left(z - z_m\right)/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right] \\
&\overset{\text{推導 3}}{=}& \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1/2}e^{\left(z - z_m\right)/2}\left[\frac{z_T}{2\pi}\sin\left(\frac{\pi z}{z_T}\right) - \cos\left(\frac{\pi z}{z_T}\right)\right]
\end{gather*}$$

### (c) proof 結構函數的導數 (Derivative of the structure function)

把【推導 6】的 $2\lambda A$ 直接代進【推導 2】(d)。

$$\begin{gather*}
\frac{dZ}{dz} &\overset{\text{推導 2(d)}}{=}& 2\lambda A\,e^{z/2}\sin\left(kz\right) \\
&\overset{\text{推導 6}}{=}& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{-z_m/2}\,e^{z/2}\sin\left(kz\right) \\
&\overset{\text{推導 3}}{=}& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{\left(z - z_m\right)/2}\sin\left(\frac{\pi z}{z_T}\right)
\end{gather*}$$

### (d) proof 歸一化的自洽性 (Consistency of the normalization)

把【證明 (c)】代到 $z = z_m$，看它是否真的等於 $1$。

$$\begin{gather*}
Z'\left(z_m\right) &\overset{\text{證明 (c)}}{=}& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{0}\sin\left(\frac{\pi z_m}{z_T}\right) \\
&\overset{\text{推導 5(a)}}{=}& \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}\left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{-1/2} \\
&=& 1
\end{gather*}$$

### (e) solve $z_m$ 的數值 (Numerical value of $z_m$)

把【定義 1】的 $z_T$ 代進【推導 4】。

$$\begin{gather*}
\frac{2\pi}{z_T} &\overset{\text{定義 1}}{\approx}& \frac{6.2832}{1.6194} \\
\frac{2\pi}{z_T} &\approx& 3.8799 \\
\frac{\pi z_m}{z_T} &\overset{\text{推導 4}}{=}& \pi + \tan^{-1}\left(-3.8799\right) \\
\frac{\pi z_m}{z_T} &\approx& 3.1416 - 1.3187 \\
\frac{\pi z_m}{z_T} &\approx& 1.8229 \\
\frac{z_m}{z_T} &=& \frac{1.8229}{\pi} \\
\frac{z_m}{z_T} &\approx& 0.5803 \\
z_m &\overset{\text{定義 1}}{\approx}& 0.5803 \times 1.6194 \\
z_m &\approx& 0.9397
\end{gather*}$$

+++

## 結構解釋

### $e^{z/2}$ 這個包絡的意義

【推導 1】(b) 的代換 $Z = e^{z/2}Y$ 不是技巧，是**物理**。

對數氣壓座標下，密度按 $\rho \propto e^{-z}$ 遞減（見 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【推導 1】）。波動往上傳播時，能量密度 $\rho\left|Z'\right|^{2}$ 若要守恆，振幅就必須按 $\rho^{-1/2} \propto e^{z/2}$ 增長 —— 這正是 $e^{z/2}$ 的來源。

同一件事在方程式層面的表現是：【定義 2】那個一階導數項 $-\dfrac{dZ}{dz}$（也就是 $\mathcal{D}_z$ 中的 $-1$）**唯一的作用**就是製造這個指數包絡。把它吸收掉之後，剩下的 $Y$ 就滿足最單純的簡諧方程式（【推導 1】(b)），與 Boussinesq 情形完全一樣。

### 本徵值為什麼是 $\dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}$ 而不是 $\dfrac{\pi^{2}}{z_T^{2}}$

那個 $\dfrac{1}{4}$ 就是上面 $e^{z/2}$ 的代價：【推導 2】(a) 的 $k^{2} = \lambda - \dfrac{1}{4}$。

換句話說，**分離常數被「密度遞減」墊高了 $1/4$**。這對等效重力波速有實質影響：

$$\bar{c}^{2} = \frac{R\Gamma}{\lambda} = \frac{R\Gamma}{\dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}}$$

代入 $R = 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$、$\Gamma = 23.79 \ \text{K}$、$z_T = 1.6194$：

$$\begin{gather*}
\lambda &\approx& 3.7636 + 0.25 \\
\lambda &\approx& 4.0136 \\
\bar{c}^{2} &\approx& \frac{287 \times 23.79}{4.0136} \\
\bar{c}^{2} &\approx& 1701 \ \text{m}^{2}\cdot\text{s}^{-2} \\
\bar{c} &\approx& 41.25 \ \text{m}\cdot\text{s}^{-1}
\end{gather*}$$

若忽略那個 $1/4$，$\lambda$ 會變成 $3.7636$，$\bar{c}$ 變成 $42.6 \ \text{m}\cdot\text{s}^{-1}$ —— 相差約 $3\%$，看似不大，但 Lamb 參數 $\epsilon \propto \bar{c}^{-2}$ 會差 $6\%$，直接影響所有赤道波的頻散關係。$\bar{c}$ 與 $\epsilon$ 的正式定義見 [傅立葉轉換至淺水系統](Fourier_Transform_to_Shallow_Water_System.md)。

### 為什麼 $Z'$ 是純正弦，而 $Z$ 不是

【推導 2】(d) 是本篇最漂亮的一步：套上 $z = 0$ 的邊界條件之後，$\dfrac{dZ}{dz}$ 的 $\cos$ 項**恰好整個消失**，只剩 $\sin\left(kz\right)$。

這件事有兩個後果：

1. **上邊界條件變得極簡** —— $Z'(z_T) = 0$ 直接給出 $\sin\left(kz_T\right) = 0$，本徵值量子化（【推導 3】），完全不必解超越方程式。
2. **加熱剖面的形狀被鎖定** —— $T, w, Q$ 都掛在 $Z'$ 上（見 [水平結構方程組的分離](Separation_into_Horizontal_Structure_System.md)），所以模式的加熱剖面必然是「$e^{z/2}\sin\left(\pi z/z_T\right)$」這個上下都歸零、單峰、峰值偏上（$z_m \approx 0.58\,z_T$）的形狀。論文正是拿這個形狀去對觀測，發現與西太平洋暖池的加熱剖面幾乎重合。

反觀 $Z$ 本身（【證明 (b)】）帶著 $\sin$ 與 $\cos$ 兩項，在對流層中層**變號**。這就是為什麼 $u, v, \phi, q$ 這幾個場**上下對流層反號**，而 $T, w, Q$ 不會。
