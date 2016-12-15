POSデータの加工　ReadMe 

1. インプットファイルであるinput.csvをfrequency_ver4-1.pyで読み込み、
   output1.txtへ出力。この時の出力書式は、「商品コード 会員番号 売上総数」

2. sort output1.txt >output2.txtをコマンド上で入力する。これにより、
　　ソートされたoutput1.txtの中身をoutput2.txtへ出力する。

3. frequency_ver4-2.pyでoutput2.txtを読み込み、同じ「商品コード：会員番号」を持つ行の売　　上総数を合計し、「商品コード：会員番号	合計された売上総数」という書式で
　　result.txtへ出力。

