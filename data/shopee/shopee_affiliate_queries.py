product_offer_v2_query = '''
query Fetch($page: Int) {
  productOfferV2(
    listType: 2,
    sortType: 2,
    page: $page,
    limit: 50
  ) {
    nodes {
      productName
      itemId
      commissionRate
      commission
      price
      sales
      imageUrl
      shopName
      productLink
      offerLink
      periodStartTime
      periodEndTime
      priceMin
      priceMax
      productCatIds
      ratingStar
      priceDiscountRate
      shopId
      shopType
      sellerCommissionRate
      shopeeCommissionRate
    }
    pageInfo {
      page
      limit
      hasNextPage
      scrollId
    }
  }
}
'''
