/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
    webpack: (config, { isServer }) => {
        if (!isServer) {
            config.resolve.fallback = {
                ...config.resolve.fallback,
                fs: false,
                net: false,
                tls: false
            }
        }
        config.externals = [...(config.externals || []), '@mapbox/node-pre-gyp']
        return config
    },
    experimental: {
        serverActions: {
            bodySizeLimit: '50mb',
        },
    },
    middlewareClientMaxBodySize: 52428800,
    images: {
        remotePatterns: [
            {
                protocol: 'http',
                hostname: 'localhost',
                port: '8000',
                pathname: '/static/**'
            }
        ]
    }
}

module.exports = nextConfig
