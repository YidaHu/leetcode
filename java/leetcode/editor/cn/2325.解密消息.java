//<p>给你字符串 <code>key</code> 和 <code>message</code> ，分别表示一个加密密钥和一段加密消息。解密 <code>message</code> 的步骤如下：</p>
//
//<ol> 
// <li>使用 <code>key</code> 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 <strong>顺序</strong> 。</li> 
// <li>将替换表与普通英文字母表对齐，形成对照表。</li> 
// <li>按照对照表 <strong>替换</strong> <code>message</code> 中的每个字母。</li> 
// <li>空格 <code>' '</code> 保持不变。</li> 
//</ol>
//
//<ul> 
// <li>例如，<code>key = "<em><strong>hap</strong></em>p<em><strong>y</strong></em> <em><strong>bo</strong></em>y"</code>（实际的加密密钥会包含字母表中每个字母 <strong>至少一次</strong>），据此，可以得到部分对照表（<code>'h' -&gt; 'a'</code>、<code>'a' -&gt; 'b'</code>、<code>'p' -&gt; 'c'</code>、<code>'y' -&gt; 'd'</code>、<code>'b' -&gt; 'e'</code>、<code>'o' -&gt; 'f'</code>）。</li> 
//</ul>
//
//<p>返回解密后的消息。</p>
//
//<p>&nbsp;</p>
//
//<p><strong>示例 1：</strong></p>
//
//<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/08/ex1new4.jpg" style="width: 752px; height: 150px;" /></p>
//
//<pre>
//<strong>输入：</strong>key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
//<strong>输出：</strong>"this is a secret"
//<strong>解释：</strong>对照表如上图所示。
//提取 "<em><strong>the</strong></em> <em><strong>quick</strong></em> <em><strong>brown</strong></em> <em><strong>f</strong></em>o<em><strong>x</strong></em> <em><strong>j</strong></em>u<em><strong>mps</strong></em> o<em><strong>v</strong></em>er the <em><strong>lazy</strong></em> <em><strong>d</strong></em>o<em><strong>g</strong></em>" 中每个字母的首次出现可以得到替换表。
//</pre>
//
//<p><strong>示例 2：</strong></p>
//
//<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/08/ex2new.jpg" style="width: 754px; height: 150px;" /></p>
//
//<pre>
//<strong>输入：</strong>key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
//<strong>输出：</strong>"the five boxing wizards jump quickly"
//<strong>解释：</strong>对照表如上图所示。
//提取 "<em><strong>eljuxhpwnyrdgtqkviszcfmabo</strong></em>" 中每个字母的首次出现可以得到替换表。
//</pre>
//
//<p>&nbsp;</p>
//
//<p><strong>提示：</strong></p>
//
//<ul> 
// <li><code>26 &lt;= key.length &lt;= 2000</code></li> 
// <li><code>key</code> 由小写英文字母及 <code>' '</code> 组成</li> 
// <li><code>key</code> 包含英文字母表中每个字符（<code>'a'</code> 到 <code>'z'</code>）<strong>至少一次</strong></li> 
// <li><code>1 &lt;= message.length &lt;= 2000</code></li> 
// <li><code>message</code> 由小写英文字母和 <code>' '</code> 组成</li> 
//</ul>
//
//<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li></div></div><br><div><li>👍 41</li><li>👎 0</li></div>
/**
 * @author YidaHu
 */
package leetcode.editor.cn;

import java.util.HashMap;

class Solution2325 {
    public static void main(String[] args) {
        Solution solution = new Solution2325().new Solution();
        System.out.println(solution.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"));
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public String decodeMessage(String key, String message) {
            char[] keys = key.toCharArray();
            HashMap<Character, Character> codeBook = new HashMap<>();
            char code = 'a';
            for (char c : keys) {
                if (c != ' ' && !codeBook.containsKey(c)) {
                    codeBook.put(c, code);
                    code++;
                }
            }
            char[] ret = new char[message.length()];
            char[] messages = message.toCharArray();
            for (int i = 0; i < messages.length; i++) {
                if (messages[i] == ' ') {
                    ret[i] = ' ';
                } else {
                    ret[i] = codeBook.getOrDefault(messages[i], ' ');
                }
            }
            return String.valueOf(ret);

        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}

