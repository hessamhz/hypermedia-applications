import { defineEventHandler, getQuery, readBody } from 'h3';

export default defineEventHandler(async (event) => {
  const apiBase = 'https://the-hive.space/api/v1';
  const path = event.context.params._ || '';
  const query = getQuery(event);

  const url = new URL(`${apiBase}/${path}`);
  Object.keys(query).forEach((key) => url.searchParams.append(key, query[key]));

  const response = await fetch(url, {
    method: event.method,
    headers: event.headers,
    body:
      event.method !== 'GET' && event.method !== 'HEAD'
        ? await readBody(event)
        : undefined,
  });

  event.node.res.statusCode = response.status;

  return await response.json();
});
