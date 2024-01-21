# hash_function_compare
4種類のハッシュ関数 MD5, SHA-256, Scrypt, Bscrypt の実行時間を測定します．
## 実行環境
- Python
- pyscrypt module
- bcrypt module

## 使い方
### 各ハッシュ関数の出力値と平均実行時間を確かめたいとき
```
hash_function_compare $ python main.py
```
### scryptのcostパラメータと実行時間の関係を確かめたいとき
```
hash_function_compare $ python scrypt_cost_param_evaluate.py
```

### bcryptのcostパラメータと実行時間の関係を確かめたいとき
```
hash_function_compare $ python bcrypt_cost_param_evaluate.py
```