const fastify = require('fastify')({ logger: true });
const { serverConfig } = require('../config');

fastify.get('/', async (request, reply) => ({ message: 'Server listens' }));

module.exports.startServer = async () => {
    try {
        await fastify.listen(serverConfig.port);
        fastify.log.info(`listening on ${fastify.server.address().port}`);
    } catch (error) {
        fastify.log.error(error);
        process.exit(1);
    }
};
