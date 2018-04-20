const webpack = require('webpack');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: {
        testBundle: './test.jsx',
        //indexBundle: './index'
    },
    context : __dirname + '/static_src',
    output: {
        path: __dirname + '/static/build',
        filename: NODE_ENV == 'development' ? '[name].js' : '[name]-[hash].js',
        publicPath: '/static/build/',
        library: '[name]'
    },

    devtool: NODE_ENV === 'development' ? 'cheap-module-source-map' : false,

    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    watch: NODE_ENV === 'development',

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: __dirname + '/static_src',
                loader: 'babel-loader?presets[]=react&presets[]=es2015&presets[]=stage-1'
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /\.(png|jpg|gif)$/,
                loader: 'url-loader?limit=4096&name=[path][name].[ext]'
            }
        ]
    },

    resolve: {
        modules: [`${__dirname}/static_src`, 'node_modules'],
        extensions: ['.js', '.jsx']
    }
};

if (NODE_ENV !== 'development') {
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false,
                drop_console: true,
                unsafe: true
            }
        })
    );
}
