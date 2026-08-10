# 方程式索引表 (Equations Index)

本頁是 **Theory_Playground 自己的**方程式索引，只收錄 `01_Derivations/` 底下**已經逐式證明過**的結論。

**用途**：撰寫新的推導時，凡是**本知識庫已經證明過**的式子，一律用**帶超連結的【已知】卡片**直接引用，
**不得重證**（見推導風格規範 `PC-NTU/.claude/skills/derivation-style-review/SKILL.md` §10「引用免證」）。
寫新推導前**先查本表**，不要重讀整個知識庫；證出新的可引用結論後，**回頭補一列**。

**單一職責原則**：本表**只收錄 Theory_Playground 內部已證的方程式**。
外部知識庫（如 [Advanced Atmospheric Dynamics](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/intro.html)）
的推導由該庫自行維護索引（`PC-NTU/Advanced-Atmospheric-Dynamics/equations_index.md`），
本庫的 notebook 只在【已知】卡片內以超連結引用，這樣外部改動時本表不必跟著改。

引用卡片寫法：

```markdown
* **【已知 1】 [遞迴關係 (Recurrence relation)](連結)：** 此式已於本庫 ⟨出處⟩ 完整證明，此處直接引用不再重證

  $$\hat{y}\,\mathcal{H}_n = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
```

**連結慣例**：
- 有 proof 小節 anchor 的，連到 anchor（anchor 取自標題中的**英文**；改英文標題＝改 anchor，本表要同步更新）。
- 只有頁面層級 anchor 的，連到 `.html` 頁面本身。
- 連結一律走 `_build/html` 的線上網址，這樣在 notebook 內、GitHub 上、Jupyter Book 內都點得開。

---

## Calculus

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 高斯 × Hermite 重疊積分 (Gaussian–Hermite overlap integral) | `\int_{-\infty}^{\infty}\exp\left[-\frac{(\hat{y}-\hat{y}_0)^{2}}{\hat{b}_0^{2}}\right]\mathcal{H}_n(\hat{y})\,d\hat{y} = \left(\frac{2\pi\hat{b}_0^{2}}{2+\hat{b}_0^{2}}\right)^{1/2}\left(\frac{2-\hat{b}_0^{2}}{2+\hat{b}_0^{2}}\right)^{n/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4-\hat{b}_0^{4}}\right]\mathcal{H}_n\!\left(\frac{2\hat{y}_0}{(4-\hat{b}_0^{4})^{1/2}}\right)` | [Gaussian_Hermite_Integral #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Calculus/Gaussian_Hermite_Integral.html#a-proof-hermite-gaussian-hermite-overlap-integral) | $0 \le \hat{b}_0 < 2^{1/2}$；$\mathcal{H}_n$ 為歸一化 Hermite 函數。＝ Schubert (2006) $(B.1)$。同頁附**積分表 T1–T7** |
| 窄高斯極限的自洽性 (Narrow-Gaussian limit) | `\lim_{\hat{b}_0 \to 0}\frac{1}{\hat{b}_0}\int_{-\infty}^{\infty}\exp\left[-\frac{(\hat{y}-\hat{y}_0)^{2}}{\hat{b}_0^{2}}\right]\mathcal{H}_n(\hat{y})\,d\hat{y} = \pi^{1/2}\,\mathcal{H}_n(\hat{y}_0)` | [Gaussian_Hermite_Integral #b-verify](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Calculus/Gaussian_Hermite_Integral.html#b-verify-consistency-in-the-narrow-gaussian-limit) | 高斯的 delta 函數表示；上式的一致性檢查 |
| 黃金比例高斯積分 (Golden-ratio Gaussian integral) | `\int_{-\infty}^{+\infty} \frac{e^{-x^2}\sin^2(x^2)}{x^2}\,dx = \sqrt{\pi}\left(\sqrt{\phi}-1\right)` | [golden_ratio_gaussian_integral](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Calculus/golden_ratio_gaussian_integral.html) | $\phi$ 為黃金比例；用分部積分＋倍角／半角公式 |

## Coordinate_System

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 球座標動量方程式 (Momentum equation in spherical coordinates) | `\frac{Du}{Dt} + \left(2\Omega + \frac{u}{R\cos\phi}\right)(w\cos\phi - v\sin\phi) = -\frac{1}{\rho R\cos\phi}\frac{\partial P}{\partial \lambda} + \text{RHS}_{\hat{i}}`（另兩分量同頁） | [spherical_coordinate_transformation_momentum_equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/spherical_coordinate_transformation_momentum_equation.html) | 由旋轉基底的全質導數導出；含曲率項與科氏項，未做尺度分析 |
| 圓柱座標動量方程式 (Momentum equation in cylindrical coordinates) | `\frac{Du}{Dt} - \frac{v^2}{r} - fv = -\frac{1}{\rho}\frac{\partial P}{\partial r} + \text{RHS}_{\hat{r}}`（另兩分量同頁） | [cylindrical_coordinate_transformation_momentum_equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/cylindrical_coordinate_transformation_momentum_equation.html) | 颱風中心座標；$f$ 平面 |
| 圓柱座標散度算子 (Divergence operator in cylindrical coordinates) | `\nabla \cdot \mathbf{A} = \frac{1}{r}\frac{\partial [r A_r]}{\partial r} + \frac{1}{r}\frac{\partial A_\lambda}{\partial \lambda} + \frac{\partial A_z}{\partial z}` | [Divergence_Operator_in_Cylindrical_Coordinates](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/Divergence_Operator_in_Cylindrical_Coordinates.html) | 任意向量場 $\mathbf{A}$；基底向量隨位置旋轉 |
| 圓柱座標相對渦度 (Relative vorticity in cylindrical coordinates) | `\vec{\zeta}\cdot\hat{z} = \frac{1}{r}\left(\frac{\partial (rv)}{\partial r} - \frac{\partial u}{\partial \lambda}\right)`（另兩分量同頁） | [cylindrical_coordinate_transformation_Relative_Vorticity](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/cylindrical_coordinate_transformation_Relative_Vorticity.html) | $\vec{\zeta} \overset{\text{def}}{=} \nabla\times\vec{V}$ |

## Differential_Equations

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| Sturm–Liouville 正交性 (Sturm–Liouville orthogonality) | `\int_{z_b}^{z_t}\Psi_m(z)\,\Psi_n(z)\,w(z)\,dz = 0 \quad (\lambda_m \neq \lambda_n)` | [Sturm_Liouville_Orthogonality #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Sturm_Liouville_Orthogonality.html#a-proof-orthogonality) | 正則問題：**有限閉區間**、齊次邊界條件、$p>0$、$w>0$、本徵值相異 |
| Sturm–Liouville 展開係數 (Expansion coefficient) | `q_m = \frac{\int_{z_b}^{z_t} F(z)\,\Psi_m(z)\,w(z)\,dz}{\int_{z_b}^{z_t} \Psi_m^2(z)\,w(z)\,dz}` | [Sturm_Liouville_Orthogonality #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Sturm_Liouville_Orthogonality.html#b-proof-expansion-coefficient) | 同上，另需本徵函數集完備 |
| Hermite 函數遞迴關係 (Recurrence relation of $\mathcal{H}_n$) | `\hat{y}\,\mathcal{H}_n(\hat{y}) = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})` | [Hermite_Functions_and_Recurrence #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#a-proof-recurrence-relation) | $\mathcal{H}_n \overset{\text{def}}{=} \left(\pi^{1/2}2^{n}n!\right)^{-1/2}H_n\,e^{-\hat{y}^{2}/2}$；約定 $\mathcal{H}_{-1} \equiv 0$。＝ Schubert (2006) $(4.13)$ |
| Hermite 函數微分關係 (Derivative relation of $\mathcal{H}_n$) | `\frac{d\mathcal{H}_n(\hat{y})}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})` | [Hermite_Functions_and_Recurrence #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#b-proof-derivative-relation) | 同上。＝ Schubert (2006) $(4.14)$ |
| 最低兩階 Hermite 函數 (Lowest two orders of $\mathcal{H}_n$) | `\mathcal{H}_0(\hat{y}) = \pi^{-1/4}e^{-\hat{y}^{2}/2}, \qquad \mathcal{H}_1(\hat{y}) = 2^{1/2}\pi^{-1/4}\hat{y}\,e^{-\hat{y}^{2}/2}` | [Hermite_Functions_and_Recurrence #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#c-proof-lowest-order-explicit-form) | 數值遞迴的起始值；$\mathcal{H}_1$ 由 $\mathcal{H}_0$ 與遞迴關係生成 |
| 諧振子本徵值 (Harmonic oscillator eigenvalue) | `\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n(\hat{y}) = -(2n+1)\,\mathcal{H}_n(\hat{y})` | [Hermite_Orthonormality_and_Oscillator_Eigenvalue #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.html#a-proof-harmonic-oscillator-eigenvalue) | 只用遞迴＋微分關係推出，不需 $H_n$ 的 ODE |
| Hermite 函數正交歸一性 (Orthonormality of $\mathcal{H}_n$) | `\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y} = \begin{cases}1, & n'=n\\ 0, & n'\neq n\end{cases}` | [Hermite_Orthonormality_and_Oscillator_Eigenvalue #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.html#d-proof-orthonormality) | **無窮區間 $(-\infty,\infty)$** ＋高斯衰減使邊界項消失（與 Sturm–Liouville 那篇的有限區間前提不同）。＝ Schubert (2006) $(4.18)$ |

## Fluid_Dynamics_in_Cylindrical_Coordinates

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 梯度風平衡 (Gradient wind balance) | `\frac{v^{2}}{r} + fv = \frac{\partial\phi}{\partial r}` | [Gradient_Wind_Balance](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Gradient_Wind_Balance.html) | 軸對稱、定常、無徑向加速；anelastic 近似下 $\frac{1}{\rho}\frac{\partial p}{\partial r} \to \frac{\partial\phi}{\partial r}$ |
| 擾動靜力平衡 (Hydrostatic balance for perturbations) | `\frac{\partial\phi}{\partial z} = \frac{g}{\theta_0}\theta` | [Hydrostatic_Balance_for_Perturbations](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Hydrostatic_Balance_for_Perturbations.html) | $\theta$ 為位溫**擾動量**；Boussinesq／anelastic 基本態 $\theta_0$ |
| 軸對稱連續方程式 (Axisymmetric continuity equation) | `\frac{1}{r}\frac{\partial(\rho r u)}{\partial r} + \frac{\partial(\rho w)}{\partial z} = 0` | [Axisymmetric_Continuity_Equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Continuity_Equation.html) | 軸對稱（$\partial/\partial\lambda = 0$）；anelastic（$\rho = \rho(z)$） |
| 軸對稱熱力學能量方程式 (Axisymmetric thermodynamic energy equation) | `\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + w\frac{\partial\theta}{\partial z} = \frac{\theta}{T}\frac{Q}{c_p}` | [Axisymmetric_Thermodynamic_Energy_Equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Thermodynamic_Energy_Equation.html) | 軸對稱；$Q$ 為非絕熱加熱率 |
| 軸對稱切向動量方程式 (Axisymmetric tangential momentum equation) | `\frac{\partial v}{\partial t} + u\left(f + \zeta\right) + w\frac{\partial v}{\partial z} = X` | [Axisymmetric_Tangential_Momentum_Equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Tangential_Momentum_Equation.html) | 軸對稱；$\zeta = \frac{1}{r}\frac{\partial(rv)}{\partial r}$；$X$ 為摩擦等外力 |
| 軸對稱穩定度矩陣行列式 (Determinant of the stability matrix) | `\det\left(\mathbf{S}_{\text{cyl}}\right) = \rho^{2}\left(AC - B^{2}\right)` | [Axisymmetric_Stability_Matrix](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Stability_Matrix.html) | 軸對稱擾動的線性穩定度分析；$A,B,C$ 見下一列 |
| Eliassen 結構參數 (Eliassen structural parameters) | `\rho A = \frac{g}{\theta_0}\frac{\partial\theta}{\partial z}, \quad \rho C = \left(f + \frac{2v}{r}\right)\left(f + \zeta\right), \quad \rho B = -\frac{g}{\theta_0}\frac{\partial\theta}{\partial r} = -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}` | [Eliassen_Secondary_Circulation_Coefficients](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Eliassen_Secondary_Circulation_Coefficients.html) | 靜力穩定度 / 慣性穩定度 / 斜壓度；$\rho B$ 的第二種寫法需熱力風平衡 |
| 穩定度矩陣與 Jacobian 的關係 (Stability matrix vs. Jacobian) | `AC - B^{2} = \frac{1}{\rho^{2}r}\left(f + \frac{2v}{r}\right)J(M, b)` | [Axisymmetric_Stability_Matrix_and_Jacobian_Matrix](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Stability_Matrix_and_Jacobian_Matrix.html) | $M$ 為絕對角動量、$b$ 為浮力；$J$ 為 $(r,z)$ 平面的 Jacobian |
| 結構參數與 PV 的關係 (Structural parameters vs. PV) | `(\rho A)(\rho C) - (\rho B)^{2} = \left(f + \frac{2v}{r}\right)PV_b` | [Relation_between_Axisymmetric_Structural_Parameters_and_PV](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Relation_between_Axisymmetric_Structural_Parameters_and_PV.html) | 軸對稱；$PV_b$ 為浮力型位渦 |
| Eliassen 次環流方程式 (Eliassen transverse circulation equation) | `\frac{\partial}{\partial r}\left[\frac{A}{r}\frac{\partial\psi}{\partial r} + \frac{B}{r}\frac{\partial\psi}{\partial z}\right] + \frac{\partial}{\partial z}\left[\frac{B}{r}\frac{\partial\psi}{\partial r} + \frac{C}{r}\frac{\partial\psi}{\partial z}\right] = \frac{\partial J}{\partial r} - \frac{\partial F}{\partial z}` | [Eliassen_Transverse_Equation](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Eliassen_Transverse_Equation.html) | 軸對稱、質量連續（流函數 $\psi$）；橢圓性需 $AC - B^{2} > 0$ |

## Fluid_Dynamics_Variable_Coordinate_Physics

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| Ertel PV 與浮力 PV 的關係 (Relation between PV and $PV_b$) | `PV = \left(\frac{\theta_0}{\rho_0 g}\right)PV_b` | [Relation_Between_PV_and_PVb](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_Variable_Coordinate_Physics/PV_Representations_and_Mappings/Relation_Between_PV_and_PVb.html) | Boussinesq／anelastic 基本態 $\rho_0,\ \theta_0$ 為常數 |

## Atmospheric_Dynamics

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 壓力–輻散方程式 (Pressure–divergence equation with heating) | `D - \frac{\partial}{\partial t}\left[\frac{\partial}{\partial z}\left[\frac{1}{N^{2}}\frac{\partial\Phi}{\partial z}\right]\right] = -\frac{\partial Q}{\partial z}` | [Vertical_Structure_Equation #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Atmospheric_Dynamics/Vertical_Structure_Equation.html#a-proof) | 線性化 Boussinesq；強迫是加熱的**垂直梯度**，不是加熱本身 |
| 模態投影 (Modal projection) | `\hat{D}_m + \frac{1}{c_m^{2}}\frac{\partial\hat{\Phi}_m}{\partial t} = \int_{z_b}^{z_t}\left(-\frac{\partial Q}{\partial z}\right)\Psi_m(z)\,dz` | [Vertical_Structure_Equation #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Atmospheric_Dynamics/Vertical_Structure_Equation.html#b-proof-m) | 垂直結構方程式的本徵函數 $\Psi_m$；每個模態即一組淺水系統，等效深度 $h_m = c_m^{2}/g$ |
| External mode 的本徵函數與本徵值 (External-mode eigenfunction) | `\Psi_0 = \text{const}, \qquad \frac{1}{c_0^{2}} = 0` | [Vertical_Structure_Equation #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Atmospheric_Dynamics/Vertical_Structure_Equation.html#c-proof-external-mode) | 剛蓋邊界條件 |
| 內部加熱不投影到 external mode | `\hat{D}_0 = \int_{z_b}^{z_t}\left(-\frac{\partial Q}{\partial z}\right)\Psi_0(z)\,dz = 0` | [Vertical_Structure_Equation #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Atmospheric_Dynamics/Vertical_Structure_Equation.html#d-proof-external-mode) | 剛蓋；純內部加熱（$Q$ 在上下邊界為零） |

## Equatorial_Beta_Plane_Dynamics

本節收錄 Schubert & Masarik (2006)
[*Potential vorticity aspects of the MJO*](../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb)
推導鏈的 16 篇。**閱讀順序即依賴順序**（禁止前向引用）：

```
B1 → C1 → C2            場方程與 PV 原理（C2 是物理引擎）
D1 → D2                 垂直分離
E1 → E2 → E3 → E4       正規模態（E2 是整套展開的合法性來源）
F1 → F2 → F3            端點① 受迫解
G1                      端點② PV 尾流
H1 → H2                 端點③ 可逆性原理
I1                      端點④ 平衡頻散關係
```

數學工具層（`A1`–`A3`）在上方的 `Differential_Equations` 與 `Calculus` 兩節。
括號中的 $(x.y)$ 為原論文式號，僅供對照，notebook 內一律走【已知】卡片引用法。

### B1–C2 場方程與 PV 原理

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 對數氣壓線性化原始方程組 (Log-pressure linearized primitive equations) $(2.1)$ | `\frac{\partial u}{\partial t} - \beta y v + \frac{\partial \phi}{\partial x} = -\alpha u` ／ `\frac{\partial v}{\partial t} + \beta y u + \frac{\partial \phi}{\partial y} = -\alpha v` ／ `\frac{\partial \phi}{\partial z} = RT` ／ `\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w = 0` ／ `\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p}` | [B1 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#a-proof-zonal-momentum-equation) | 赤道 $\beta$ 平面（$f = \beta y$）；繞靜止基本態線性化；準靜力；Rayleigh 摩擦與 Newtonian 冷卻共用 $\alpha$。**$z$ 無因次故 $w$ 的單位是 $\left[\text{s}^{-1}\right]$** |
| 對數氣壓連續方程式的 $-w$ 項 (The extra $-w$ term) | `\frac{\partial \omega}{\partial P} = \frac{\partial w}{\partial z} - w` | [B1 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#d-proof-continuity-equation) | $\omega = -Pw$、$P = p_0e^{-z}$；$-w$ 來自密度指數遞減 |
| 赤道渦度方程式 (Equatorial vorticity equation) $(2.4)$ | `\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right) + \beta y\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + \beta v = 0` | [C1 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#a-proof-vorticity-equation) | 由 $(2.1)$ 兩條動量方程交叉微分；$\beta v$ 來自 $\partial\left(\beta y\right)/\partial y = \beta$ |
| 位勢–輻散方程式 (Geopotential–divergence equation) $(2.5)$ | `\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} - R\Gamma\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) = \kappa\left(\frac{\partial}{\partial z} - 1\right)Q` | [C1 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#b-proof-geopotentialdivergence-equation) | 需 $\Gamma$ 為常數（才能穿過 $\partial/\partial z - 1$） |
| 位渦距平 (Potential vorticity anomaly) $(2.7)$ | `q = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z}` | [C2 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#a-proof-emergence-of-the-potential-vorticity-anomaly) | 消去 $(2.4)(2.5)$ 之間的水平輻散後**自動浮現**的組合 |
| 赤道 PV 方程式 (Equatorial PV equation) $(2.6)$ | `\frac{\partial q}{\partial t} + \beta v = -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q` | [C2 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#b-proof-pv-potential-vorticity-equation) | 同上 |
| ★ 源項在赤道恆為零 (Vanishing source at the equator) | `\left.\frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q\right\|_{y = 0} = 0` | [C2 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#c-proof-vanishing-of-the-source-at-the-equator) | 與加熱強度無關；**全文物理引擎** |
| ★ 高斯加熱下源項的極值位置 (Source extrema) | `y_{\text{ext}} = \pm\frac{b_0}{2^{1/2}}` | [C2 #e-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#e-proof-location-of-the-source-extrema) | 加熱經向剖面為中心在赤道的高斯；$b_0 = 450 \ \text{km}$ 時 $\approx \pm318 \ \text{km}$ |

### D1–D2 垂直分離

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 垂直結構方程式 (Vertical structure equation) $(3.1)$ | `\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)Z` | [D1 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Vertical_Structure_Equation_in_Log_Pressure.html#a-proof-eigenvalue-of-the-first-vertical-internal-mode) | 剛蓋 $Z'(0) = Z'(z_T) = 0$；第一垂直內模態；$z_T \approx 1.619$ |
| 垂直結構函數 (Vertical structure function) $(3.2)$ | `Z(z) = \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1/2}e^{(z-z_m)/2}\left[\frac{z_T}{2\pi}\sin\frac{\pi z}{z_T} - \cos\frac{\pi z}{z_T}\right]` | [D1 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Vertical_Structure_Equation_in_Log_Pressure.html#b-proof-normalized-vertical-structure-function) | 同上；歸一化取 $Z'(z_m) = 1$，$z_m \approx 0.5803\,z_T$ |
| 垂直結構函數的導數 (Its derivative) $(3.3)$ | `Z'(z) = \left(1 + \frac{z_T^{2}}{4\pi^{2}}\right)^{1/2}e^{(z-z_m)/2}\sin\frac{\pi z}{z_T}` | [D1 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Vertical_Structure_Equation_in_Log_Pressure.html#c-proof-derivative-of-the-structure-function) | 同上；$T, w, Q$ 掛在此函數上 |
| 水平結構方程組 (Horizontal structure system) $(3.5)$ | `\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y} - \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)\hat{w} = 0`（另四條同頁） | [D2 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Separation_into_Horizontal_Structure_System.html#d-proof-separation-of-the-continuity-equation) | 只激發第一垂直內模態；**$u,v,\phi \propto Z$ 而 $T,w,Q \propto Z'$ 是被靜力方程與連續方程逼出來的** |

### E1–E4 正規模態轉換

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 淺水系統與線性算符 (Shallow water system and the operator) $(4.3)(4.6)(4.7)$ | `\left(\alpha - \frac{imc}{a}\right)\hat{\boldsymbol{\eta}}_m + \mathcal{L}\hat{\boldsymbol{\eta}}_m = \kappa\hat{\mathbf{Q}}_m` | [E1 #e-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#e-proof-vector-form) | 隨波定常（$\xi = x - ct$）；緯向週期 $2\pi a$ |
| 等效重力波速 (Equivalent gravity wave speed) | `\bar{c}^{2} = R\Gamma\left[\left(\frac{\pi}{z_T}\right)^{2} + \frac{1}{4}\right]^{-1} \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}` | [E1 #f-solve](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#f-solve-numerical-value-of-the-equivalent-gravity-wave-speed) | 等效深度 $H_{\text{eq}} = \bar{c}^{2}/g \approx 173 \ \text{m}$；Lamb 參數 $\epsilon = 4\Omega^{2}a^{2}/\bar{c}^{2} \approx 507.3$ |
| 總能量原理 (Total energy principle) $(2.2)(2.3)$ | `\frac{d\mathcal{E}}{dt} = -2\alpha\mathcal{E} + \mathcal{G}` | [E2 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#a-proof-total-energy-principle) | 緯向週期、經向衰減、剛蓋；科氏力不做功、位勢通量總積分為零 |
| ★ 能量內積權重的來源 (Origin of the $1/\bar{c}^{2}$ weight) $(4.8)$ | `\mathcal{E} = \frac{I_Z}{2}\iint\left[\hat{u}^{2} + \hat{v}^{2} + \frac{1}{\bar{c}^{2}}\hat{\phi}^{2}\right]dx\,dy` | [E2 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#c-proof-1-bar-c-2-origin-of-the-1-bar-c-2-weight) | 關鍵是 $\int Z'^{2}e^{-z}dz = \lambda\int Z^{2}e^{-z}dz$；**內積不是猜的，是算出來的** |
| ★ 算符的反厄米性 (Skew-Hermiticity) | `\mathcal{L}^{\dagger} = -\mathcal{L}` | [E2 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#d-proof-skew-hermiticity-of-the-operator) | 相對於能量內積；需本徵函數赤道捕捉。**整套正規模態展開的合法性來源** |
| Matsuno 頻散關係 (Matsuno dispersion relation) $(4.10)$ | `\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} = \epsilon^{1/2}\left(2n + 1\right)` | [E3 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Matsuno_Dispersion_Relation.html#a-proof-notation-mapping-and-scale-restoration) | 與 AAD project2_1 的 $\omega^{2}-k^{2}-\frac{k}{\omega}-1=2n$ 等價（$\omega = \epsilon^{1/4}\hat{\nu}$、$k = \epsilon^{-1/4}m$） |
| Kelvin 波的本徵值 (Kelvin wave eigenvalue) | `\epsilon^{1/2}\hat{\nu}_{m,-1,2} = m` | [E3 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Matsuno_Dispersion_Relation.html#c-proof-kelvin-kelvin-wave-eigenvalue) | 令 $V = 0$ 單獨求得；有界性淘汰另一根。形式上即 $(4.10)$ 的 $n = -1$ |
| 赤道波本徵函數 (Equatorial wave eigenfunctions) $(4.11)$ | `\mathbf{K}_{mnr} = A_{mnr}\left(\epsilon^{1/4}\left[\mathcal{P}\mathcal{H}_{n+1} + \mathcal{M}\mathcal{H}_{n-1}\right],\ -i\left(\epsilon\hat{\nu}^{2}-m^{2}\right)\mathcal{H}_n,\ \bar{c}\epsilon^{1/4}\left[\mathcal{P}\mathcal{H}_{n+1} - \mathcal{M}\mathcal{H}_{n-1}\right]\right)^{\mathsf{T}}` | [E4 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#a-proof-explicit-form-of-the-eigenfunctions) | $n \ge 0$；$\mathcal{P} = \left(\epsilon^{1/2}\hat{\nu}+m\right)\left(\frac{n+1}{2}\right)^{1/2}$、$\mathcal{M} = \left(\epsilon^{1/2}\hat{\nu}-m\right)\left(\frac{n}{2}\right)^{1/2}$ |
| 歸一化常數 (Normalization constant) $(4.15)$ | `A_{mnr} = \left[\epsilon^{1/2}(n+1)\left(\epsilon^{1/2}\hat{\nu}+m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}-m\right)^{2} + \left(\epsilon\hat{\nu}^{2}-m^{2}\right)^{2}\right]^{-1/2}` | [E4 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#b-proof-n-ge-0-normalization-constant-for-n-ge-0) | $n \ge 0$；Kelvin 波為 $A_{m,-1,2} = 2^{-1/2}\pi^{-1/4}$ |
| 本徵函數的正交歸一 (Orthonormality) $(4.17)$ | `\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) = \delta_{nn'}\delta_{rr'}` | [E4 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#d-proof-orthonormality) | 非簡併；簡併情形（$m=0,n>0,r=0$）另由 $(A.1)$ 處理 |
| 緯向對稱羅斯貝模態 (Zonally symmetric Rossby modes) $(A.1)$ | `\mathbf{K}_{0n0} = \left(2n+1\right)^{-1/2}\left(\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1},\ 0,\ \bar{c}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]\right)^{\mathsf{T}}` | [E4 #e-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#e-proof-eigenfunctions-of-the-zonally-symmetric-rossby-modes) | $m \to 0$ 極限；對應**定常的地轉平衡緯向噴流**（$\beta y U + d\Phi/dy = 0$） |

### F1–F3 端點① 受迫解

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| ★ 受迫解（一行除法）(Forced response) $(4.21)$ | `\hat{\eta}_{mnr} = \frac{\kappa\hat{Q}_{mnr}}{\alpha + i\left(\nu_{mnr} - \frac{cm}{a}\right)}` | [F1 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Forced_Response_of_Equatorial_Modes.html#c-proof-forced-response) | 需 $\alpha > 0$；受迫阻尼振子形式，$\nu_{mnr} = cm/a$ 時共振 |
| 加熱總量與 $y_0$ 無關 (Total heating) | `\iint \hat{Q}\,d\xi\,dy = \pi^{1/2}Q_0a_0b_0` | [F2 #a-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Projection_of_a_Moving_Heat_Source.html#a-proof-y-0-the-total-heating-is-independent-of-y-0) | 加熱為升餘弦（緯向）$\times$ 高斯（經向）$(4.1)$ |
| 加熱的緯向傅立葉係數 (Zonal Fourier coefficient) $(4.5)$ | `\hat{Q}_m(y) = \frac{\pi Q_0}{2\left[\pi^{2}-\left(ma_0/a\right)^{2}\right]}\frac{\sin\left(ma_0/a\right)}{m}\exp\left[-\left(\frac{y-y_0}{b_0}\right)^{2}\right]` | [F2 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Projection_of_a_Moving_Heat_Source.html#b-proof-zonal-fourier-coefficient) | $a_0 < \pi a$；$\sin\mu/\mu$ 的第一零點在 $m \approx 16$ |
| 加熱的模態投影 (Modal projection of the heating) $(4.22)$ | 見該頁（含 $\chi^{(n\pm1)/2}$ 與 $\mathcal{H}_{n\pm1}(\eta)$ 兩個因子） | [F2 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Projection_of_a_Moving_Heat_Source.html#c-proof-n-ge-0-modal-projection-for-n-ge-0) | 需 $\hat{b}_0 = \epsilon^{1/4}b_0/a < 2^{1/2}$（本文 $\approx 0.335$）；用到 $(B.1)$ 兩次 |
| ★ $y_0 = 0$ 時偶數 $n$ 不被激發 (Even modes vanish) | `\left.\hat{Q}_{mnr}\right\|_{\hat{y}_0 = 0} = 0 \quad \left(n \ \text{even}\right)` | [F2 #e-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Projection_of_a_Moving_Heat_Source.html#e-proof-even-modes-are-not-excited-when-the-convection-is-centred-on-the-equator) | 宇稱：$\Phi_{mnr} \propto \mathcal{H}_{n\pm1}$，$n$ 偶則為奇函數。含 $n = 0$ 混合羅斯貝–重力波 |
| 位渦的譜係數 (Spectral PV coefficient) $(4.26)$ | `\hat{q}_{mnr} = A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\hat{\nu}_{mnr}}\right)\hat{\eta}_{mnr}` | [F3 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Physical_Field_Recovery_and_Zero_Kelvin_PV.html#c-proof-spectral-coefficient-of-the-pv) | 需 $\nu_{mnr} \neq 0$；每個模態的 PV **只含單一個 $\mathcal{H}_n$** |
| ★★ Kelvin 波的位渦為零 (Zero Kelvin PV) | `\hat{q}_{m,-1,2} = 0` | [F3 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Physical_Field_Recovery_and_Zero_Kelvin_PV.html#d-proof-kelvin-zero-potential-vorticity-of-the-kelvin-wave) | **代數恆等式，非近似。** 端點③在對流東側失效的根源 |
| 垂直速度的還原 (Vertical velocity recovery) $(4.27)$ | `w = \frac{Z'(z)}{R\Gamma}\sum_{m}\sum_{n,r}i\nu_{mnr}\hat{\eta}_{mnr}\Phi_{mnr}(\hat{y})e^{im\xi/a}` | [F3 #e-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Physical_Field_Recovery_and_Zero_Kelvin_PV.html#e-proof-recovery-of-the-vertical-velocity) | $\omega = -p_0e^{-z}w$ 才是常見的 $p$ 座標垂直速度 |

### G1 端點② PV 尾流

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| PV 尾流的解析解 (Analytic PV wake) $(5.2)$ | `q = -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}\left(\frac{\pi^{2}}{\pi^{2}+\alpha^{2}\tau_{\mathrm{p}}^{2}}\right)F(\xi)\,\beta y\exp\left[-\left(\frac{y-y_0}{b_0}\right)^{2}\right]Z(z)` | [G1 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/PV_Wake_of_a_Moving_Heat_Source.html#b-proof-solution-inside-the-convective-region) | **刻意忽略 Rossby 項 $\beta v$**（只剩正確強度的 $68\%$）；$\tau_{\mathrm{p}} = a_0/c$、$\tau_{\mathrm{c}} = \bar{c}^{2}/(\kappa Q_0)$ |
| 尾流的緯向結構（後方）(Zonal structure behind) $(5.3)$ | `F(\xi) = \frac{\sinh\left[(\alpha/c)a_0\right]}{(\alpha/c)a_0}\exp\left[\frac{\alpha}{c}\xi\right]` | [G1 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/PV_Wake_of_a_Moving_Heat_Source.html#c-proof-solution-behind-the-convective-region) | $\xi \le -a_0$；$F = 0$ 於 $\xi \ge a_0$ |
| 三個控制參數 (Three control parameters) | `\frac{c}{\alpha} \approx 1728 \ \text{km}, \quad \frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}} \approx 5.9, \quad \frac{y_0}{b_0}` | [G1 #e-solve](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/PV_Wake_of_a_Moving_Heat_Source.html#e-solve-numerical-values-of-the-three-control-parameters) | 分別控制**衰減長度／強度／南北不對稱**；$\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ ＝對流通過期間翻轉幾次 |

### H1–I1 端點③④ 可逆性原理與平衡頻散關係

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| ★ 赤道平衡關係 (Equatorial balance relation) | `\phi = \beta y\,\psi` | [H1 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Invertibility_Principle.html#b-proof-local-balance-relation) | 線性平衡 ＋ **$\beta y$ 緩變**；漏掉 $\beta\partial\psi/\partial y$，**在赤道最不準** |
| 赤道 PV 可逆性原理 (Invertibility principle) $(6.2)$ | `\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} = q` | [H1 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Invertibility_Principle.html#c-proof-invertibility-principle) | 橢圓型；邊界條件 $\psi \to 0$（$\|y\|\to\infty$）、$\partial\psi/\partial z = 0$（$z = 0, z_T$） |
| 可逆性原理的譜形式 (Spectral form) $(6.3)$ | `\epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m - m^{2}\hat{\psi}_m = a^{2}\hat{q}_m` | [H1 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Invertibility_Principle.html#d-proof-invertibility-principle-in-spectral-space) | 左端算符即量子諧振子算符（$\beta y$ 用了兩次的結果） |
| ★ 反演的一行除法 (One-line inversion) $(6.6)$ | `\hat{\psi}_{mn} = -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}` | [H2 #b-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Hermite_Transform_Solution_of_Invertibility.html#b-proof-one-line-division-in-spectral-space) | 分母恆為正（最小值 $\epsilon^{1/2} \approx 22.5$，**無共振**）；反演天生平滑化 |
| 平衡場的還原 (Balanced field recovery) $(6.8)(6.9)$ | `\begin{pmatrix}U_{mn}\cr V_{mn}\cr \Phi_{mn}\end{pmatrix} = \begin{pmatrix}\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]\cr im\mathcal{H}_n\cr \bar{c}\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]\end{pmatrix}e^{im\xi/a}` | [H2 #d-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Hermite_Transform_Solution_of_Invertibility.html#d-proof-recovery-of-the-rotational-wind-and-mass-fields) | **恰為 $(4.11)$ 的羅斯貝波極限** —— 可逆性原理只看得見羅斯貝波 |
| 平衡模式的羅斯貝頻散關係 (Balanced Rossby dispersion relation) $(7.3)$ | `\frac{\nu_{mn}}{2\Omega} = -\frac{m}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}` | [I1 #c-proof](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Balanced_Rossby_Dispersion_Relation.html#c-proof-dispersion-relation-of-the-balanced-model) | 無黏絕熱；$v \approx \partial\psi/\partial x$。即 $(4.10)$ 丟掉 $\epsilon\hat{\nu}^{2}$ 的結果 |
| 平衡近似的失效區域 (Where it fails) | `\left.\frac{\epsilon\hat{\nu}^{2}}{m^{2}}\right\|_{n=0,m=1} \approx 0.92` | [I1 #e-solve](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Balanced_Rossby_Dispersion_Relation.html#e-solve-where-the-approximation-fails) | 低波數 $n = 0$（sectoral harmonics）重力波項與 PV 項同量級；$n = 3, m = 1$ 僅 $0.02$ |
