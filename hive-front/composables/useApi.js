// export const useApi = (request, opts) => {
//   const config = useRuntimeConfig();

//   return useFetch(request, { baseURL: config.public.baseURL, ...opts });
// };
export function useApi(path, options = {}) {
  const config = useRuntimeConfig();
  return useFetch(`/api/${path}`, {
    ...options,
    baseURL: config.public.apiBase,
  });
}
