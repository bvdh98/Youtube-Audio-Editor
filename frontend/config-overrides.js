const webpack = require("webpack");
module.exports = function override(config) {
  const fallback = config.resolve.fallback || {};
  Object.assign(fallback, {
    "m3u8stream": require.resolve("m3u8stream"),
    "miniget": require.resolve("miniget"),
    "sax": require.resolve("sax"),
    "stream-http": require.resolve("stream-http"), 
    "stream-browserify": require.resolve("stream-browserify"), 
    "https-browserify": require.resolve("https-browserify"),
    "query-string": require.resolve("query-string"),  
  });
  config.resolve.fallback = fallback;
  config.plugins = (config.plugins || []).concat([
    new webpack.ProvidePlugin({
      process: "process/browser",
      Buffer: ["buffer", "Buffer"],
    }),
  ]);
  return config;
};
