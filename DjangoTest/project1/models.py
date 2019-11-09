from django.db import models

# Create your models here.
class Type(models.Model):
    class Meta():
        verbose_name="商品类别"
        verbose_name_plural="商品类别"
        # ordering = ["-id"]
    Type_name = models.CharField(max_length=50,verbose_name="类型")



    def __str__(self):
        return self.Type_name

class Goods(models.Model):
    class Meta():
        verbose_name="商品"
        verbose_name_plural="商品"
    goods_name = models.CharField(max_length=50,verbose_name="商品名称")
    image = models.ImageField(upload_to="media/image",verbose_name="图片")
    price = models.FloatField("价钱",blank=True,null="True")
    #blank 默认为False,在admin管理平台中必填.为True可以不填
    #null 默认为False,不能为空.为True可以为空
    is_delete = models.IntegerField(default=1)

    def __str__(self):
        return self.goods_name

class Goods_type(models.Model):
    class Meta():
        verbose_name="商品分类表"
        verbose_name_plural="商品分类表"
    goods = models.ForeignKey(to="Goods",on_delete=models.CASCADE)
    type = models.ForeignKey(to="Type",on_delete=models.CASCADE)