# -*- coding: utf-8 -*-
"""產生 Vertical_Structure_Equation.ipynb「物理解釋」段落所需的三張圖。

用法（在本檔所在目錄執行）：
    py make_figures.py
輸出到 ../pic/：
    heating_gradient_forcing.png      對應 物理解釋 (a)
    vertical_modes_equivalent_depth.png  對應 物理解釋 (b)
    external_mode_cancellation.png    對應 物理解釋 (c)(d)

圖上一律使用英文標籤，避免建置環境缺中文字型時出現豆腐字。
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G, THETA0 = 9.81, 300.0          # 重力加速度 [m/s^2]、參考位溫 [K]
N2 = 1.0e-4                      # 浮力頻率平方 N^2 [s^-2]
ZT = 16000.0                     # 剛蓋高度 z_t [m]
NZ = 400

PIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pic")


def grid(nz=NZ, zt=ZT):
    """cell-centered 垂直網格。"""
    dz = zt / nz
    return (np.arange(nz) + 0.5) * dz, dz


def vertical_modes(z, dz, n_mode=4, N2=N2):
    """解垂直結構方程式 d/dz[(1/N^2) dPsi/dz] = -(1/c^2) Psi，剛蓋(Neumann)邊界。"""
    nz = z.size
    A = np.zeros((nz, nz))
    for i in range(nz):
        if i > 0:
            A[i, i - 1] = -1.0
            A[i, i] += 1.0
        if i < nz - 1:
            A[i, i + 1] = -1.0
            A[i, i] += 1.0
    A /= (N2 * dz ** 2)
    lam, vec = np.linalg.eigh(A)
    lam, vec = lam[:n_mode], vec[:, :n_mode]
    vec /= np.sqrt((vec ** 2).sum(0) * dz)          # 正規化 int Psi^2 dz = 1
    for m in range(n_mode):
        ref = vec[:, m].mean() if m == 0 else vec[0, m]
        if ref < 0:
            vec[:, m] *= -1
    c = np.where(lam > 1e-14, 1.0 / np.sqrt(np.abs(lam)), np.inf)
    return c, vec


def heating(z, deep_K_day=8.0, z_peak=6500.0, z_wid=12000.0,
            surf_K_day=0.0, h_s=1500.0, zt=ZT):
    """深對流加熱（上下邊界嚴格歸零）＋ 可選的地表感熱（下邊界不歸零）。"""
    shape = np.sin(np.pi * z / zt) * np.exp(-((z - z_peak) / z_wid) ** 2)
    s = deep_K_day / 86400.0 * shape / shape.max()
    s = s + surf_K_day / 86400.0 * np.exp(-z / h_s)
    q_b = G / THETA0 * s
    return q_b / N2                                  # 層結縮放後的 Q [m/s]


# ============================================================
# 圖一：加熱本身 vs 加熱的垂直梯度（物理解釋 (a)）
# ============================================================
def fig_heating_gradient(z, dz):
    Q_deep = heating(z)
    Q_unif = np.full_like(z, Q_deep.max() * 0.6)     # 垂直均勻的加熱
    km = z / 1000.0

    fig, ax = plt.subplots(1, 2, figsize=(11, 5), sharey=True)

    ax[0].plot(Q_deep, km, lw=2.2, color="tab:blue", label="deep convective heating")
    ax[0].plot(Q_unif, km, lw=2.2, ls="--", color="tab:red", label="vertically uniform heating")
    ax[0].set_xlabel(r"$Q(z)$   [m s$^{-1}$]")
    ax[0].set_ylabel("height [km]")
    ax[0].set_title(r"(a) the heating itself,  $Q$", fontsize=11)

    ax[1].plot(-np.gradient(Q_deep, dz), km, lw=2.2, color="tab:blue")
    ax[1].plot(-np.gradient(Q_unif, dz), km, lw=2.8, ls="--", color="tab:red")
    ax[1].axvline(0, color="k", lw=1.0)
    ax[1].set_xlabel(r"$-\partial Q/\partial z$   [s$^{-1}$]")
    ax[1].set_title(r"(b) what the waves actually feel,  $-\partial Q/\partial z$", fontsize=11)
    ax[1].annotate("uniform heating gives\nZERO forcing, however strong",
                   xy=(0, 8), xytext=(0.04, 0.78), textcoords="axes fraction",
                   color="tab:red", fontsize=10, ha="left",
                   arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.4))

    for a in ax:
        a.grid(alpha=.3)
        a.set_ylim(0, ZT / 1000.0)
    ax[0].legend(fontsize=9, loc="upper right")
    fig.suptitle("Heating drives waves only through its vertical gradient", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PIC, "heating_gradient_forcing.png"), dpi=110)
    plt.close(fig)


# ============================================================
# 圖二：垂直模態與等效深度（物理解釋 (b)）
# ============================================================
def fig_modes(z, dz):
    c, PSI = vertical_modes(z, dz)
    km = z / 1000.0
    h = c ** 2 / G

    fig, ax = plt.subplots(1, 2, figsize=(11, 5),
                           gridspec_kw={"width_ratios": [1.25, 1]})

    for m in range(4):
        ax[0].plot(PSI[:, m], km, lw=2.2, label=r"$\Psi_%d$" % m)
    ax[0].axvline(0, color="k", lw=1.0)
    ax[0].set_xlabel(r"$\Psi_m(z)$   [m$^{-1/2}$]")
    ax[0].set_ylabel("height [km]")
    ax[0].set_ylim(0, ZT / 1000.0)
    ax[0].set_title("(a) vertical eigenfunctions", fontsize=11)
    ax[0].legend(fontsize=9, loc="lower left")
    ax[0].grid(alpha=.3)

    idx = np.arange(1, 4)
    ax[1].bar(idx, h[1:4], 0.55, color="tab:green")
    for i in idx:
        ax[1].text(i, h[i] * 1.15, "$c_%d$ = %.0f m/s\n$h_%d$ = %.0f m" % (i, c[i], i, h[i]),
                   ha="center", fontsize=9)
    ax[1].text(0, h[1] * 3.0, r"$m=0$ : $c_0=\infty$" "\n" r"$h_0=\infty$",
               ha="center", fontsize=9, color="tab:red")
    ax[1].bar([0], [h[1] * 2.6], 0.55, color="tab:red", alpha=.35, hatch="//")
    ax[1].set_yscale("log")
    ax[1].set_ylim(1, h[1] * 60)
    ax[1].set_xticks([0, 1, 2, 3])
    ax[1].set_xlabel("vertical mode $m$")
    ax[1].set_ylabel(r"equivalent depth $h_m = c_m^2/g$   [m]")
    ax[1].set_title("(b) each mode = its own shallow-water system", fontsize=11)
    ax[1].grid(alpha=.3, axis="y")

    fig.suptitle("One 3-D problem splits into infinitely many 2-D shallow-water problems", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PIC, "vertical_modes_equivalent_depth.png"), dpi=110)
    plt.close(fig)


# ============================================================
# 圖三：external mode 的正負面積相消（物理解釋 (c)(d)）
# ============================================================
def fig_cancellation(z, dz):
    c, PSI = vertical_modes(z, dz)
    psi0 = PSI[:, 0].mean()                          # Psi_0 是常數
    km = z / 1000.0

    cases = [
        ("(a) purely internal heating", heating(z), "tab:blue"),
        ("(b) with surface sensible heat", heating(z, surf_K_day=4.0), "tab:orange"),
    ]

    fig, ax = plt.subplots(1, 2, figsize=(11, 5), sharey=True, sharex=True)
    for k, (title, Q, col) in enumerate(cases):
        integrand = -np.gradient(Q, dz) * psi0
        total = integrand.sum() * dz
        pos = np.clip(integrand, 0, None).sum() * dz
        neg = np.clip(integrand, None, 0).sum() * dz

        a = ax[k]
        a.fill_betweenx(km, 0, np.clip(integrand, 0, None), color="tab:red", alpha=.45,
                        label="positive area = %+.2e" % pos)
        a.fill_betweenx(km, 0, np.clip(integrand, None, 0), color="tab:blue", alpha=.45,
                        label="negative area = %+.2e" % neg)
        a.plot(integrand, km, lw=2.0, color="k")
        a.axvline(0, color="k", lw=1.0)
        a.set_xlabel(r"$-\dfrac{\partial Q}{\partial z}\,\Psi_0$   [m$^{-1/2}$ s$^{-1}$]")
        a.set_title(title, fontsize=11)
        a.grid(alpha=.3)
        note = (r"$\int = %+.1e \approx 0$" % total) if k == 0 else (r"$\int = %+.1e \neq 0$" % total)
        a.text(0.04, 0.94, note + "\n" + ("areas cancel exactly" if k == 0
                                          else r"boundary term $\Psi_0 Q(z_b)$ survives"),
               transform=a.transAxes, fontsize=10, va="top",
               bbox=dict(boxstyle="round", fc="w", ec="0.6"))
        a.legend(fontsize=8, loc="lower right")

    ax[0].set_ylabel("height [km]")
    ax[0].set_ylim(0, ZT / 1000.0)
    fig.suptitle(r"$\Psi_0$ is constant, so the external-mode projection only sees the boundaries",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PIC, "external_mode_cancellation.png"), dpi=110)
    plt.close(fig)


# ===== 主程式執行區 =====
if __name__ == "__main__":
    os.makedirs(PIC, exist_ok=True)
    z, dz = grid()
    fig_heating_gradient(z, dz)
    fig_modes(z, dz)
    fig_cancellation(z, dz)
    print("圖片已輸出到：", os.path.normpath(PIC))
    for f in sorted(os.listdir(PIC)):
        print("  -", f)
