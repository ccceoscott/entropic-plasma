import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Phase 43: Eliminates 3-4x RAM spike during Rollup compilation
  productionBrowserSourceMaps: false,
  
  // Phase 43: Redactive logging — never allow console bleed in production
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production'
      ? { exclude: ['error', 'warn'] }
      : false,
  },
};

export default nextConfig;
