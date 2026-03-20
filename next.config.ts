import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  productionBrowserSourceMaps: false,
  experimental: {
    memoryBasedWorkersCount: true
  }
};

export default nextConfig;
