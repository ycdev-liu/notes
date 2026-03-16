


// 加上 export，别的文才就能看到它
export function calculateTotal(level, ...prices) {
    const goodTotal = prices.reduce((a, b) => a + b, 0);
    const shippingCost = (level === "VIP" || goodTotal >= 200) ? 0 : 20;
    return { goodTotal, shippingCost, finalBill: goodTotal + shippingCost };
}

export const shopName = "极客超市"; // 变量也可以导出