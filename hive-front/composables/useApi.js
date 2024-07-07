export function useApi(path, options = {}) {
  const config = useRuntimeConfig();
  return useFetch(`/api/${path}`, {
    ...options,
    baseURL: config.public.apiBase,
  });
}
