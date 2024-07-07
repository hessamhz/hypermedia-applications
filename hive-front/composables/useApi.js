export function useApi(path, options = {}) {
  const config = useRuntimeConfig();
  return useFetch(`${path}`, {
    ...options,
    baseURL: config.public.baseURL,
  });
}
