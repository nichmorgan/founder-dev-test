const gatewayHost = import.meta.env.VITE_GATEWAY_HOST;
if (!gatewayHost) throw "GATEWAY_HOST envvar is required!";

export default Object.freeze({
  gatewayHost,
});
