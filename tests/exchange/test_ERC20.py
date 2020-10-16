def test_ERC20(w3, HAY_token, pad_bytes32):
    a0, a1 = w3.eth.accounts[:2]
    assert PHY_token.name() == pad_bytes32('HAY Token')
    assert PHY_token.symbol() == pad_bytes32('HAY')
    assert PHY_token.decimals() == 18
    assert PHY_token.totalSupply() == 100000*10**18
    assert PHY_token.balanceOf(a0) == 100000*10**18
    PHY_token.transfer(a1, 1*10**18, transact={})
    assert PHY_token.balanceOf(a0) == 100000*10**18 - 1*10**18
    assert PHY_token.balanceOf(a1) == 1*10**18
