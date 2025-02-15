# global
import mxnet as mx
from typing import Tuple, Union, Optional, Iterable

# local
from ivy import default_device, dtype_from_str, default_dtype
from ivy.functional.backends.mxnet import _mxnet_init_context
from ivy.functional.backends.mxnet import _1_dim_array_to_flat_array


def zeros(shape: Union[int, Tuple[int]],
          dtype: Optional[type] = None,
          device: Optional[mx.context.Context] = None) \
        -> mx.ndarray.ndarray.NDArray:
    cont = _mxnet_init_context(default_device(device))
    if len(shape) == 0 or 0 in shape:
        return _1_dim_array_to_flat_array(mx.nd.zeros((1,), ctx=cont).astype(dtype))
    return mx.nd.zeros(shape, ctx=cont).astype(dtype)


def ones(shape: Union[int, Tuple[int]],
         dtype: Optional[type] = None,
         device: Optional[str] = None) \
        -> mx.ndarray.ndarray.NDArray:
    cont = _mxnet_init_context(default_device(device))
    shape = [shape] if shape is not isinstance(shape, Iterable) else shape
    if len(shape) == 0 or 0 in shape:
        return _1_dim_array_to_flat_array(mx.nd.ones((1,), ctx=cont).astype(dtype))
    return mx.nd.ones(shape, ctx=cont).astype(dtype)


def ones_like(x : mx.ndarray.ndarray.NDArray,
              dtype : Optional[Union[type, str]] = None,
              dev : Optional[Union[mx.context.Context, str]] = None) \
        -> mx.ndarray.ndarray.NDArray:
    if x.shape == ():
        return mx.nd.array(1., ctx=_mxnet_init_context(default_device(dev)))
    mx_ones = mx.nd.ones_like(x, ctx=_mxnet_init_context(default_device(dev)))
    return mx_ones if dtype is None else mx_ones.astype(dtype)

  
def tril(x: mx.ndarray.ndarray.NDArray,
         k: int = 0) \
         -> mx.ndarray.ndarray.NDArray:
    return mx.np.tril(x, k)


def empty(shape: Union[int, Tuple[int]],
          dtype: Optional[type] = None,
          device: Optional[mx.context.Context] = None) \
        -> mx.ndarray.ndarray.NDArray:
    cont = _mxnet_init_context(default_device(device))
    return mx.nd.empty(shape, dtype_from_str(default_dtype(dtype)), cont)
