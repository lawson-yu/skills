# 面向可测试性的接口设计

良好的接口会让测试变得自然：

1. **接收依赖，不要创建依赖**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **返回结果，不要产生副作用**

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Hard to test
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **保持较小的表面积**
   - 更少的方法 = 需要更少的测试
   - 更少的参数 = 更简单的测试设置
