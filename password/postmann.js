let b = pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Response body contains 'Hello, World!'", function () {
    pm.expect(pm.response.text()).to.include("Hello, World!");
});