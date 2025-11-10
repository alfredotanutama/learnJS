const applePrice = 5000;
const appleQty = 3;
const bananaPrice = 10000;
const bananaQty = 2;
const couponDisc = 0.1;

const totalBuyApple = (applePrice * appleQty);
const totalBuyBanana = (bananaPrice * bananaQty);
const total = totalBuyApple + totalBuyBanana;
const totalDiscount = couponDisc * total;
const subTotal = total - totalDiscount;
console.log(subTotal);